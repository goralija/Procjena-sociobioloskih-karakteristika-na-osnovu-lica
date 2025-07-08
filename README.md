# Procjena sociobioloskih karakteristika na osnovu lica

# **University of Sarajevo**

## **Faculty of Electrical Engineering Sarajevo**

### **Department of Computer Science and Informatics**

**Artificial Intelligence – Academic Year 2024/2025**

# **Estimation of Sociobiological Characteristics Based on Facial Images**

---

## **Phase 1: Topic Selection and Problem Description**

### **Introduction and Motivation**

In the era of digital transformation, automatic facial image analysis has become a key component of many advanced technological systems. Our project focuses on the automatic estimation of sociobiological characteristics of individuals based on their facial photographs – specifically race, gender, and age. This presents a significant technical challenge requiring advanced deep learning algorithms, but also a socially sensitive topic that demands a careful, ethical approach.

Automatic estimation of demographic characteristics has broad practical applications, from demographic analysis and personalized user interfaces to security systems and healthcare applications. However, this field faces significant algorithmic bias challenges that can have serious social consequences.

### **Problem Description**

The problem of automatic estimation of sociobiological characteristics is complex for several key reasons:

**Genetic and Cultural Diversity**: There are enormous variations within each demographic group. People of the same race can have drastically different facial features due to genetic diversity, geographical origin, and population mixing through history.

**Undefined Boundaries**: Boundaries between demographic groups are not always clearly defined, making precise categorization particularly challenging. This is especially evident in racial classification where significant overlap exists.

**Data Bias**: Existing datasets are often not representative of the global population. Most are biased toward certain demographic groups, resulting in systems that perform well only for part of the population.

**Ethical Implications**: Automatic categorization of people by demographic characteristics carries the risk of reinforcing existing social prejudices and discrimination through algorithmic bias.

### **Key Concepts**

**Racial Classification**: The process of automatically determining a person’s racial affiliation based on facial features. It's important to note that the terms "race" and "ethnicity" are used in a scientific context, acknowledging that they are social constructs and not fully reflective of biological reality.

**Gender Estimation**: Algorithmic determination of a person’s binary gender (male/female) based on facial features. We acknowledge the limitations of this approach which does not encompass the entire spectrum of gender identities, but adhere to existing labels within available datasets.

**Age Estimation**: Algorithmic estimation of which age group a person belongs to. Instead of a precise age in years, we use age groups that reflect different life stages.

**Convolutional Neural Networks (CNNs)**: A type of deep learning specifically designed for image processing. They automatically learn hierarchical representations – from simple edges and textures to complex structures defining specific facial features.

**Algorithmic Bias**: A phenomenon where AI systems demonstrate unfair or discriminatory behavior toward certain groups. This is the central challenge of our project, which we aim to address through careful data and method selection.

### **Practical Applications**

**Demographic Analysis**: Enables automatic collection of data on population structure from large image collections, useful for social research, urban planning, and demographic policy development.

**User Interface Personalization**: The system can tailor content and presentation based on users’ demographic characteristics, improving accessibility and overall user experience.

**Forensics and Security**: Such systems can assist in identifying individuals and analyzing security footage, but this application requires special attention due to implications for privacy and civil liberties.

**Social Media Analysis**: Allows researchers to understand the demographic structure of online communities and how different groups use digital platforms.

**Marketing and Advertising**: Information can be used to better target campaigns, but under strict ethical guidelines to prevent discrimination and respect user privacy.

---

## **Phase 2: State of the Art Review**

### **Current State of the Field**

The field of automatic estimation of sociobiological characteristics from facial images has seen exponential growth in recent years, primarily due to advancements in deep learning and the availability of large datasets. However, alongside technical progress, research has highlighted serious problems of algorithmic bias in existing systems.

There is a duality between impressive technical achievements and growing ethical concerns. While modern solutions achieve over 95% accuracy on standard benchmarks, these performances often drop significantly when tested on underrepresented demographic groups.

### **Key Papers and Research**

**"Gender Shades" (Buolamwini & Gebru, 2018)**: This pioneering study revealed significant differences in the accuracy of commercial gender recognition systems, with the lowest performance for darker-skinned women. It marked a turning point in raising awareness about algorithmic bias.

**"FairFace: Face Attribute Dataset for Balanced Race, Gender, and Age" (Kärkkäinen & Joo, 2021)**: The authors introduce the FairFace dataset as a solution to the problem of unbalanced datasets, showing that models trained on this balanced dataset exhibit more consistent accuracy across demographic groups.

**"Diversity in Faces" (Merler et al., 2019)**: IBM's initiative to create a diverse and representative dataset for fairer facial analysis.

### **Methodologies and Approaches**

**Convolutional Neural Networks (CNNs)**: The dominant methodology allowing automatic learning of relevant features from images. Popular architectures include ResNet, VGGFace, and FaceNet.

**Transfer Learning**: Became standard practice. Instead of training models from scratch, one starts with a pretrained model that has already learned rich representations from millions of images.

**Multi-task Learning**: A sophisticated solution where one model simultaneously learns all three tasks (race, gender, age), allowing for shared representation learning across tasks.

### **Identified Problems and Challenges**

**Systemic Bias**: The biggest challenge in the field. Studies have shown that existing commercial systems perform significantly worse for certain demographic groups, with accuracy differences of 15-25% between best- and worst-represented groups.

**Unbalanced Datasets**: The root of many problems. When 80% of training data comes from one demographic group, the model naturally becomes biased toward that group.

**Ethical Questions**: Who gives consent for the use of images? How is privacy ensured? How is discrimination prevented? These questions have no simple answers.

### **Achieved Results**

Current state-of-the-art systems achieve:

* Gender estimation: Accuracy over 97% on balanced datasets
* Racial classification: Accuracy over 85% on the FairFace dataset
* Age estimation: Mean Absolute Error under 3 years

However, the key finding is that these performances vary significantly across demographic groups.

---

## **Phase 3: Dataset Selection, Analysis, and Preprocessing**

### **Strategic Dataset Selection**

After careful analysis of available options, we chose the **FairFace dataset**. This was not a random decision—FairFace represents a revolution in the approach to demographic classification. Unlike many existing datasets that have organically inherited bias, FairFace is consciously designed to be balanced across key demographic features.

### **Detailed FairFace Dataset Analysis**

**General Info:**
- **Source**: Developed at UCLA (Kärkkäinen & Joo, 2021)
- **Availability**: Publicly available on GitHub with clear usage terms
- **Format**: JPG images + CSV label files
- **Total Instances**: 108,501 facial images
- **Size**: ~551.4 MB
- **Resolution**: Typically between 200x200 and 500x500 pixels

**Label Structure:**
- **Race (7 classes)**: White, Black, East Asian, Southeast Asian, Indian, Middle Eastern, Latino/Hispanic
- **Gender (2 classes)**: Male, Female (50/50 distribution)
- **Age (9 groups)**: 0–2, 3–9, 10–19, 20–29, 30–39, 40–49, 50–59, 60–69, 70+

**Dataset Split:**
- Training: 86,744 (80%)
- Validation: 10,954 (10.1%)
- Test: 10,803 (9.9%)

Split is stratified, maintaining demographic proportions in all subsets.

### **Balance Analysis**
- **Race**: ~10–19% per group

   <img src="./img/dataset_distribucija_rase.png" alt="Confusion Matrix - Gender" style="height:400px;">

---

- **Gender**: Perfectly balanced (50/50)
- **Age**: Naturally varied, adult groups (20–59) most represented

   <img src="./img/dataset_distribucija_dobi.png" alt="Confusion Matrix - Gender" style="height:400px;">

---


### **Preprocessing Steps**
1. **Resize (224×224)** for ResNet compatibility
2. **ToTensor()** to convert to PyTorch format
3. **Normalize()** with ImageNet stats: mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]

### **Risks Identified**
- **Phenotypic Overlap** between race groups
- **Cultural Artifacts** (makeup, hairstyle) may bias models
- **Intersectional Effects** (e.g. older women in minority groups perform worse)

---

## **Phase 4: Model Selection, Training, and Testing**

### **Method and Framework Choice**

We used **deep learning with CNNs** due to their proven success in image tasks. Specifically, **PyTorch** was selected for its flexibility, debugging ease, and GPU support.

### **Model Architecture**
- **Backbone**: ResNet-34 pretrained on ImageNet
- **Output Layers**:
  - Race: Fully connected, 7 outputs
  - Gender: Fully connected, 2 outputs
  - Age: Fully connected, 9 outputs

This is a **multi-task model** sharing early layers and branching out at the end.

### **Training Settings**
- **Batch size**: 64
- **Optimizer**: Adam, lr=0.0001
- **Epochs**: 20
- **Image Limit**: 65,000 (due to Colab limits)

### **Limitations**
- **No validation set** used during training
  - To avoid unbalancing the training set
  - Minimized risk of Colab timeouts
  - Residual connections reduce overfitting
  - Empirical hyperparameter values used

### **Training Results**
Loss steadily dropped from ~4100 to ~250 over 20 epochs, indicating good learning.

### **Testing Pipeline**
1. Load trained model
2. Process test images
3. Predict race, gender, age
4. Save predictions to CSV
5. Generate confusion matrices for each task

### **Test Set Results**
- **Gender**: 89.9% accuracy, F1-score: 0.899

   <img src="./img/gender_confusion_matrix.png" alt="Confusion Matrix - Gender" style="height:400px;">

---

- **Race**: 60.3% accuracy, F1-score: 0.602

   <img src="./img/race_confusion_matrix.png" alt="Confusion Matrix - Race" style="height:400px;">

---

- **Age**: 51.2% accuracy, F1-score: 0.509

   <img src="./img/age_confusion_matrix.png" alt="Confusion Matrix - Age" style="height:400px;">

---


### **Confusion Matrix Insights**
- **Gender**: Very low confusion
- **Race**: Confusions between similar groups (e.g. East Asian vs. Southeast Asian)
- **Age**: Mostly adjacent class misclassifications

---

## **Phase 5: Overall Evaluation and Reflection**

### **Result Summary**
- **Gender Prediction**: High accuracy (~90%)
- **Race Prediction**: Moderate accuracy (60%) across 7 classes
- **Age Prediction**: Acceptable accuracy (51%) with most errors close to the correct class

### **Comparison with Related Work**
- Comparable or better than FairFace paper results
- Less biased than commercial systems (less disparity between groups)

### **Demographic Breakdown**
- **Gender**: Strong performance, minimal bias
- **Race**: Performance varies with group overlap, dataset limitations
- **Age**: Continuous nature of aging adds difficulty; balanced performance across ages

### **Limitations and Future Improvements**
- Add validation set with early stopping
- Use full dataset (>65k images)
- Explore modern architectures (EfficientNet, ViT)
- Tune hyperparameters, try weighted loss, regularization, data augmentation

### **Ethical Considerations**
- Less bias thanks to FairFace
- Still categorizing people by physical traits – ethical caution needed
- Use with transparency, clear disclaimers, and regular monitoring

### **Practical Impact**
- Proof-of-concept system with fairer performance
- Strong base for future research
- Highlights social and technical challenges in ethical AI

### **Conclusion**

This project demonstrated the development of a system for estimating sociobiological traits from facial images with a strong emphasis on minimizing bias. Using a balanced dataset and multi-task deep learning, we achieved solid performance while maintaining ethical responsibility.

Key contributions include:
- Balanced data usage
- Multi-task model implementation
- Demographic-aware performance analysis

Most importantly, we demonstrated that fairer AI systems are possible through careful design choices, but also emphasized that such systems should be developed and deployed with deep awareness of their ethical ramifications.


