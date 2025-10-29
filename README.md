# 🍷 Wine Quality Prediction

A machine learning project that predicts whether a wine is **Good Quality** or **Not Good Quality** based on its chemical properties.  
Built with **Python**, **scikit-learn**, and **Streamlit**.

---

## 📘 Overview

This project trains multiple classification models (Logistic Regression, Decision Tree, Random Forest, SVM, and KNN) on a wine dataset and selects the best-performing one.  
A simple **Streamlit web app** lets users input wine features and instantly get a prediction.

---

## ⚙️ Features

- Loads and preprocesses the Wine Quality dataset  
- Trains multiple ML models and compares performance  
- Saves the best model and scaler using `pickle`  
- Interactive Streamlit interface for real-time prediction  
- Clean and minimal UI with clear visual feedback  

---

## 🧠 Technologies Used

- **Python 3.11+**
- **pandas**
- **numpy**
- **scikit-learn**
- **Streamlit**
- **pickle**

---

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/wine-quality-prediction.git
cd wine-quality-prediction
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Train the model
```bash
python train_model.py
```
This will generate:
- `best_model.pkl`
- `scaler.pkl`

### 4. Run the Streamlit app
```bash
streamlit run app.py
```

---

## 🧪 Input Features

| Feature | Description |
|----------|-------------|
| Fixed Acidity | Tartaric acid (g/dm³) |
| Volatile Acidity | Acetic acid (g/dm³) |
| Citric Acid | Citric acid (g/dm³) |
| Residual Sugar | Remaining sugar after fermentation (g/dm³) |
| Chlorides | Salt content (g/dm³) |
| Free Sulfur Dioxide | Free form of SO₂ (mg/dm³) |
| Total Sulfur Dioxide | Total SO₂ (mg/dm³) |
| Density | Wine density (g/cm³) |
| pH | Acidity level |
| Sulphates | Potassium sulphate (g/dm³) |
| Alcohol | Alcohol percentage (%) |

---

## 🧩 Model Training Summary

- Multiple models tested: Logistic Regression, Decision Tree, Random Forest, SVM, and KNN  
- Accuracy compared using `accuracy_score`  
- Best model is automatically saved for deployment

---

## 🖥️ Example Prediction

**Input:**  
`alcohol = 11.5`, `pH = 3.3`, `citric acid = 0.36`, etc.

**Output:**  
✅ *This wine is likely Good Quality!* 🍇

---

## 💾 Files in This Project

```
📁 Wine Prediction/
│
├── app.py              # Streamlit web app
├── train_model.py      # Model training script
├── requirements.txt    # Dependencies
├── WineQT.csv          # Dataset
├── best_model.pkl      # Trained best model
├── scaler.pkl          # Scaler used for input normalization
└── README.md           # Project documentation
```

---

## ❤️ Acknowledgements

- Dataset: [Wine Quality Data Set - UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Wine+Quality)
- Developed by **Himanshu Khobaragade** with guidance from AI learning projects.

---

### ScreenShot

# Train Model
<img width="1146" height="599" alt="Screenshot 2025-10-29 143222" src="https://github.com/user-attachments/assets/094e6679-bb05-4742-9137-4c6b24ab18ab" />

# Output
<img width="970" height="773" alt="Screenshot 2025-10-29 142632" src="https://github.com/user-attachments/assets/90446e83-8125-4a82-92f3-d9b40d1a4f0e" />
<img width="972" height="710" alt="Screenshot 2025-10-29 143137" src="https://github.com/user-attachments/assets/350c0a7b-cbbf-470a-8f88-578069071230" />






