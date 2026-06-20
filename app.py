import streamlit as st
import pandas as pd
import pickle

# Load model
with open("diamond_knn_model.pkl", "rb") as file:
    model = pickle.load(file)

# Load preprocessor
with open("preprocessor.pkl", "rb") as file:
    preprocessor = pickle.load(file)

st.set_page_config(page_title="Diamond Price Prediction")

st.title("💎 Diamond Price Prediction using KNN")

# User Inputs
carat = st.number_input("Carat", min_value=0.1, value=1.0)
cut = st.selectbox("Cut", ["Fair", "Good", "Very Good", "Premium", "Ideal"])
color = st.selectbox("Color", ["D", "E", "F", "G", "H", "I", "J"])
clarity = st.selectbox("Clarity", ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"])
depth = st.number_input("Depth", value=61.0)
table = st.number_input("Table", value=57.0)
x = st.number_input("Length (x)", value=5.0)
y = st.number_input("Width (y)", value=5.0)
z = st.number_input("Depth (z)", value=3.0)

if st.button("Predict Price"):

    input_data = pd.DataFrame({
        "carat": [carat],
        "cut": [cut],
        "color": [color],
        "clarity": [clarity],
        "depth": [depth],
        "table": [table],
        "x": [x],
        "y": [y],
        "z": [z]
    })

    # Apply preprocessing
    processed_data = preprocessor.transform(input_data)

    # Predict
    prediction = model.predict(processed_data)[0]

    st.success(f"💰 Predicted Diamond Price: ${prediction:,.2f}")
