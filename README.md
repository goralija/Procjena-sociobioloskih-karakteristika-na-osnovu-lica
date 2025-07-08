# **Estimation of Sociobiological Characteristics Based on Facial Images**

# **University of Sarajevo**

## **Faculty of Electrical Engineering Sarajevo**

### **Department of Computer Science and Informatics**

**Artificial Intelligence – Academic Year 2024/2025**

---

## **1. Problem Overview**

With the rise of AI, analyzing facial images to estimate sociobiological traits (race, gender, age) has grown in relevance. This task poses both technical and ethical challenges due to genetic diversity, ambiguous group definitions, biased datasets, and the risk of reinforcing social stereotypes.

### **Applications**
- Demographics, UI personalization, forensics, marketing, and healthcare.

---

## **2. State of the Art**

Recent progress in deep learning, particularly Convolutional Neural Networks (CNNs), has led to high accuracy in facial attribute estimation. Key methods include transfer learning and multi-task learning. Still, commercial systems often show significant bias.

### **Notable Studies**
- **Gender Shades**: Highlighted bias in commercial classifiers.
- **FairFace**: Introduced a balanced dataset to mitigate bias.

---

## **3. Dataset & Preprocessing**

**Dataset**: FairFace (108k+ images) labeled by race (7 groups), gender (2), and age (9 groups). Split into train, validation, and test sets.
**More about dataset:** ![datasetInfo](./dataset.md)

**Balance Analysis**:
- Race: ~10–19% per group  
  <img src="./img/dataset_distribucija_rase.png" alt="Race Distribution" height="300">
  ---
  
- Gender: 50/50
  --- 
- Age: Broad distribution  
  <img src="./img/dataset_distribucija_dobi.png" alt="Age Distribution" height="300">
  ---
  

**Preprocessing**:
- Resize to 224×224
- Tensor conversion & normalization (ImageNet stats)

---

## **4. Model & Training**

**Architecture**: ResNet-34 (pretrained) with three heads for race, gender, and age (multi-task setup).

**Training**:
- Epochs: 20, Batch: 64, Optimizer: Adam (lr=0.0001)
- Subset of 65k images (due to Colab limits)

**Loss dropped** from ~4100 → ~250.

<img src="./img/loss_epochs_graph.png" alt="Gender Confusion Matrix" height="300">

---

## **5. Evaluation Results**

**Test Accuracy**:
- Gender: 89.9%  
  <img src="./img/gender_confusion_matrix.png" alt="Gender Confusion Matrix" height="300">
  ---
- Race: 60.3%  
  <img src="./img/race_confusion_matrix.png" alt="Race Confusion Matrix" height="300">
  ---
- Age: 51.2%  
  <img src="./img/age_confusion_matrix.png" alt="Age Confusion Matrix" height="300">
  ---

**Insights**:
- Gender prediction: very accurate
- Race: confusions between similar-looking groups
- Age: most errors near true class

---

## **6. Evaluation & Ethics**

**Strengths**:
- Gender classification is robust
- Race and age predictions are reasonable
- Less biased than commercial tools due to dataset balance

**Limitations**:
- No validation set used
- Limited dataset due to runtime constraints

**Future Work**:
- Use full dataset
- Add validation with early stopping
- Experiment with modern models (EfficientNet, ViT)

**Ethical Notes**:
- Bias is reduced but not eliminated
- Transparent usage and disclaimers are essential

---

## **Conclusion**

We developed a deep learning model for estimating race, gender, and age from facial images with a strong focus on fairness. Using the FairFace dataset and multi-task learning, we achieved promising results while acknowledging ethical concerns.

**Contributions**:
- Balanced data usage
- Multi-task model
- Fairness-aware evaluation

Fairer AI is achievable with deliberate data and architectural choices, but deployment must remain ethically grounded.

