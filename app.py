import streamlit as st
import pickle
import pandas as pd

# Load model
with open("diamond_knn_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("💎 Diamond Price Prediction")

carat = st.number_input("Carat", min_value=0.1)
depth = st.number_input("Depth")
table = st.number_input("Table")
x = st.number_input("Length (x)")
y = st.number_input("Width (y)")
z = st.number_input("Depth (z)")

cut = st.selectbox("Cut", ["Fair", "Good", "Very Good", "Premium", "Ideal"])
color = st.selectbox("Color", ["D", "E", "F", "G", "H", "I", "J"])
clarity = st.selectbox("Clarity", ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"])

if st.button("Predict Price"):
    data = pd.DataFrame({
        'carat':[carat],
        'cut':[cut],
        'color':[color],
        'clarity':[clarity],
        'depth':[depth],
        'table':[table],
        'x':[x],
        'y':[y],
        'z':[z]
    })

    prediction = model.predict(data)[0]
    st.success(f"Predicted Price: ${prediction:.2f}")