# 🍇 Wine Quality Prediction App (Streamlit)

import streamlit as st
import pandas as pd
import pickle
import numpy as np

# === Page Configuration ===
st.set_page_config(
    page_title="Wine Quality Prediction",
    page_icon="🍷",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# === Load Model and Scaler ===
with open("best_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# === Feature List ===
features = [
    'fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
    'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
    'pH', 'sulphates', 'alcohol'
]

# === App Title and Intro ===
st.title("🍷 Wine Quality Prediction")
st.markdown("Use this app to predict whether a wine is **Good Quality** or **Not Good Quality** based on its chemical properties.")
st.markdown("---")

# === Input Section ===
st.subheader("🧪 Enter Wine Characteristics")

input_data = []
cols = st.columns(2)  # Two columns for better layout

for i, feature in enumerate(features):
    with cols[i % 2]:
        val = st.number_input(f"{feature.capitalize()}", min_value=0.0, step=0.01)
        input_data.append(val)

# === Prepare Data for Prediction ===
input_df = pd.DataFrame([input_data], columns=features)
input_scaled = scaler.transform(input_df)

# === Predict Button ===
st.markdown("---")
if st.button("🔍 Predict Quality"):
    prediction = model.predict(input_scaled)[0]

    if prediction == 1:
        st.success("✅ This wine is likely **Good Quality** 🍇")
    else:
        st.error("❌ This wine is likely **Not Good Quality** 🍷")

# === Footer ===
st.markdown("---")
st.markdown(
    "<div style='text-align:center; font-size:14px;'>"
    "📘 Developed by: Himanshu Khobaragade | Machine Learning Mini Project"
    "</div>",
    unsafe_allow_html=True
)
st.markdown(
    "<div style='text-align:center; font-size:14px;'>"
    "Developed with ❤️ using <b>Streamlit</b> and <b>Machine Learning</b>"
    "</div>",
    unsafe_allow_html=True
)
