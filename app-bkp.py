import streamlit as st
import pandas as pd
import joblib
from models_utils import build_full_feature_df

@st.cache_resource
def load_model():
    return joblib.load("models/notebooks_generated_best_model.pkl")

model = load_model()

st.title("Poverty Probability Predictor")

country = st.selectbox("Country", ["C", "A", "D", "G", "F", "I", "J"])
age = st.number_input("Age", 0, 120, 25)
is_urban = st.selectbox("Urban?", ["Yes", "No"])
female = st.selectbox("Female?", ["Yes", "No"])
education_level = st.number_input("Education level", 0, 40, 10)
num_shocks_last_year = st.number_input("Num shocks last year", 0, 10, 0)

user_inputs = {
    "country": country,
    "age": int(age),
    "is_urban": 1 if is_urban == "Yes" else 0,
    "female": 1 if female == "Yes" else 0,
    "education_level": int(education_level),
    "num_shocks_last_year": int(num_shocks_last_year)
}

if st.button("Predict"):
    df_ready = build_full_feature_df(user_inputs)

    st.write("### DF Ready")
    st.write(df_ready)

    try:
        pred = model.predict(df_ready)[0]
        st.success(f"Poverty probability: {pred:.4f}")
    except Exception as e:
        st.error(f"Error: {e}")
