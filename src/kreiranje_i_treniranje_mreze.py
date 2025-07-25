# -*- coding: utf-8 -*-
"""Kreiranje i treniranje mreze.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Gw8pxvh_D4wVgaIq9DbOIEYJVh1sZnYB

# Osnovni importi
"""

import os
import pandas as pd
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, models
from PIL import Image
from tqdm import tqdm

"""# Mount drive-a"""

from google.colab import drive
drive.mount('/content/drive', force_remount=True)

"""# Podesena 'putanja'"""

from google.colab import drive
drive.mount('/content/drive')

import os
putanja = '/content/drive/MyDrive/[VI projekat] Procjena sociobioloskih karakteristika na osnovu slike lica '
try:
  print(os.listdir(putanja))
except Exception as e:
  izuzetak = True
os.chdir(putanja)

"""# Napravljene konstante"""

# Postavke
VERSION=1
DATA_DIR = putanja + '/dataset'
CSV_PATH = putanja + '/dataset/fairface_label_train.csv'
NUM_EPOCHS = 20
BATCH_SIZE = 50
LEARNING_RATE = 0.0018
MODEL_SAVE_PATH = putanja + '/modeli/nas_model5.pt'
MAX_IMAGES = 65000

"""# Dataset klasa"""

# Dataset klasa
class FairFaceDataset():
    def __init__(self, csv_file, img_dir, transform=None, max_images=MAX_IMAGES):
        self.img_dir = img_dir
        self.transform = transform

        self.race2idx = {'White': 0, 'Black': 1, 'Latino_Hispanic': 2,
                         'East Asian': 3, 'Southeast Asian': 4, 'Indian': 5, 'Middle Eastern': 6}
        self.gender2idx = {'Male': 0, 'Female': 1}
        self.age2idx = {'0-2': 0, '3-9': 1, '10-19': 2, '20-29': 3, '30-39': 4,
                        '40-49': 5, '50-59': 6, '60-69': 7, 'more than 70': 8}

        full_data = pd.read_csv(csv_file)
        full_data = full_data.sample(frac=1).reset_index(drop=True)  # shuffle

        # Zadrži samo redove za koje postoji slika, do max_images
        filtered_rows = []
        count = 0
        for _, row in full_data.iterrows():
            img_path = os.path.join(self.img_dir, row['file'])
            if os.path.isfile(img_path):
                filtered_rows.append(row)
                count += 1
                if count >= max_images:
                    break

        self.data = pd.DataFrame(filtered_rows)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        row = self.data.iloc[idx]
        img_path = os.path.join(self.img_dir, row['file'])
        #print(row['file'])
        image = Image.open(img_path).convert('RGB')

        race = self.race2idx[row['race']]
        gender = self.gender2idx[row['gender']]
        age = self.age2idx[row['age']]

        if self.transform:
            image = self.transform(image)

        return image, race, gender, age

"""# Instanciranje dataseta"""

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                          std=[0.229, 0.224, 0.225])
])


dataset = FairFaceDataset(CSV_PATH, DATA_DIR, transform=transform)
dataloader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True, num_workers=4)

"""# Treniranje modela"""

import matplotlib.pyplot as plt
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = models.resnet34(pretrained=True)
model.fc = nn.Linear(model.fc.in_features, 18)  # 7 + 2 + 9
model = model.to(device)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=LEARNING_RATE)

total_loss_history = []


for epoch in range(NUM_EPOCHS):
    model.train()
    total_loss = 0
    for images, race, gender, age in tqdm(dataloader, desc=f"Epoch {epoch+1}/{NUM_EPOCHS}"):
        images = images.to(device)
        race = race.to(device)
        gender = gender.to(device)
        age = age.to(device)

        outputs = model(images)
        race_out = outputs[:, :7]
        gender_out = outputs[:, 7:9]
        age_out = outputs[:, 9:]

        loss_race = criterion(race_out, race)
        loss_gender = criterion(gender_out, gender)
        loss_age = criterion(age_out, age)

        loss = loss_race + loss_gender + loss_age

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()


    total_loss_history.append((epoch + 1, total_loss))


    print(f"""
    ------------
    Epoch {epoch+1} - Loss: {total_loss/len(dataloader):.4f}
    ------------""")

    torch.save(model.state_dict(), MODEL_SAVE_PATH)
    print(f"Model saved to {MODEL_SAVE_PATH}")


epochs, losses = zip(*total_loss_history)
plt.figure(figsize=(8, 5))
plt.plot(epochs, losses, marker='o', linestyle='-', color='r')
plt.title('Loss po epohama')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.grid(True)
plt.tight_layout()
plt.show()