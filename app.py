import streamlit as st
import pandas as pd
import joblib

# ==========================================
# Load Model
# ==========================================

model = joblib.load("LaptopPricePrediction.pkl")

# ==========================================
# Page Config
# ==========================================

st.set_page_config(
    page_title="Laptop Price Prediction",
    page_icon="💻",
    layout="wide"
)

st.title("💻 Laptop Price Prediction")
st.markdown(
    """
Prediksi harga laptop menggunakan Machine Learning.

Model terbaik:
- Linear Regression

Dataset:
- Global Laptop Dataset (1.2 Million Rows)
"""
)

st.divider()

# ==========================================
# Input User
# ==========================================

col1, col2 = st.columns(2)

with col1:

    country = st.selectbox(
        "Country",
        [
            "USA",
            "Indonesia",
            "Japan",
            "Germany",
            "China",
            "India"
        ]
    )

    laptop_brand = st.selectbox(
        "Laptop Brand",
        [
            "ASUS",
            "Acer",
            "Apple",
            "Dell",
            "HP",
            "Lenovo",
            "MSI"
        ]
    )

    laptop_model = st.text_input(
        "Laptop Model",
        "Model A"
    )

    cpu_brand = st.selectbox(
        "CPU Brand",
        [
            "Intel",
            "AMD",
            "Apple"
        ]
    )

    gpu_brand = st.selectbox(
        "GPU Brand",
        [
            "NVIDIA",
            "AMD",
            "Intel"
        ]
    )

    gpu_model = st.text_input(
        "GPU Model",
        "RTX 4060"
    )

with col2:

    ram = st.number_input(
        "RAM (GB)",
        4,
        128,
        16
    )

    storage = st.number_input(
        "Storage (GB)",
        128,
        4096,
        512
    )

    cores = st.slider(
        "CPU Cores",
        2,
        32,
        8
    )

    threads = st.slider(
        "Threads",
        2,
        64,
        16
    )

    base_clock = st.number_input(
        "Base Clock",
        value=2.5
    )

    boost_clock = st.number_input(
        "Boost Clock",
        value=4.5
    )

    tdp = st.number_input(
        "TDP",
        value=65
    )

    cpu_perf = st.number_input(
        "CPU Performance",
        value=8000
    )

    gpu_perf = st.number_input(
        "GPU Performance",
        value=6000
    )

    total_perf = cpu_perf + gpu_perf

    usage = st.selectbox(
        "Usage Type",
        [
            "Gaming",
            "Office",
            "Student",
            "Creator",
            "Business"
        ]
    )

# ==========================================
# Prediction
# ==========================================

if st.button("🚀 Predict Price"):

    input_data = pd.DataFrame({

        "Country":[country],
        "Laptop_Brand":[laptop_brand],
        "Laptop_Model":[laptop_model],
        "CPU_Brand":[cpu_brand],
        "GPU_Brand":[gpu_brand],
        "GPU_Model":[gpu_model],
        "RAM_GB":[ram],
        "Storage_GB":[storage],
        "Cores":[cores],
        "Threads":[threads],
        "Base_Clock":[base_clock],
        "Boost_Clock":[boost_clock],
        "TDP":[tdp],
        "CPU_Performance":[cpu_perf],
        "GPU_Performance":[gpu_perf],
        "Total_Performance":[total_perf],
        "Usage_Type":[usage]

    })

    prediction = model.predict(input_data)[0]

    st.success(
        f"Predicted Price : ${prediction:,.2f}"
    )

    kurs = 16500

    st.info(
        f"≈ Rp {prediction*kurs:,.0f}"
    )
