# ===============================
# 🍷 Wine Quality Prediction Model
# ===============================

import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

# === Load Dataset ===
print("\n📂 Loading dataset...")
url = "WineQT.csv"
data = pd.read_csv(url, sep=',')
print("✅ Dataset loaded successfully!\n")

# Display column names for verification
print("🧾 Columns in dataset:")
print(list(data.columns), "\n")

# === Clean and Preprocess Data ===
print("⚙️ Cleaning data...")

# Drop 'Id' column if present
if 'Id' in data.columns:
    data = data.drop('Id', axis=1)
    print("🗑️ Dropped 'Id' column.")

# Convert 'quality' into binary class (Good = 1, Not Good = 0)
data['quality'] = data['quality'].apply(lambda x: 1 if x >= 7 else 0)
print("✅ Converted 'quality' column into binary classification.\n")

# Split features and labels
X = data.drop('quality', axis=1)
y = data['quality']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# === Feature Scaling ===
print("📏 Scaling features...")
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
print("✅ Feature scaling complete.\n")

# === Define Models ===
models = {
    "Logistic Regression": LogisticRegression(),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(random_state=42),
    "SVM": SVC(),
    "KNN": KNeighborsClassifier()
}

# === Train and Evaluate Models ===
print("🤖 Training models...\n")
results = {}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    results[name] = acc
    print(f"📊 {name}: {acc * 100:.2f}%")

# === Identify Best Model ===
best_model_name = max(results, key=results.get)
best_model = models[best_model_name]
print(f"\n🏆 Best Model: {best_model_name} with Accuracy = {results[best_model_name] * 100:.2f}%")

# === Save Model and Scaler ===
print("\n💾 Saving model and scaler...")
with open("best_model.pkl", "wb") as f:
    pickle.dump(best_model, f)

with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("✅ Model and Scaler saved successfully!")
print("🎯 Training complete! Ready for Streamlit app.\n")
