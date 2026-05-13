import streamlit as st
import pickle
import numpy as np

@st.cache_resource
def load_model():
    with open("model/predictor.pickle", "rb") as file:
        return pickle.load(file)

model = load_model()

st.title("Laptop Price Predictor")

ram = st.number_input("RAM (GB)", min_value=1, max_value=128, value=8)
weight = st.number_input("Weight (Kg)", min_value=0.5, max_value=10.0, value=2.0)

touchscreen = st.checkbox("Touchscreen")
ips = st.checkbox("IPS")

company = st.selectbox("Company", [
    "acer", "apple", "asus", "dell", "hp", "lenovo", "msi", "other", "toshiba"
])

typename = st.selectbox("Type Name", [
    "2in1convertible", "gaming", "netbook", "notebook", "ultrabook", "workstation"
])

opsys = st.selectbox("Operating System", [
    "linux", "mac", "windows", "other"
])

cpu = st.selectbox("CPU", [
    "amd", "intelcorei3", "intelcorei5", "intelcorei7", "other"
])

gpu = st.selectbox("GPU", [
    "amd", "intel", "nvidia"
])

def add_one_hot(feature_list, options, selected_value):
    for item in options:
        if item == selected_value:
            feature_list.append(1)
        else:
            feature_list.append(0)

if st.button("Predict Price"):
    feature_list = []

    feature_list.append(int(ram))
    feature_list.append(float(weight))
    feature_list.append(1 if touchscreen else 0)
    feature_list.append(1 if ips else 0)

    company_list = ['acer', 'apple', 'asus', 'dell', 'hp', 'lenovo', 'msi', 'other', 'toshiba']
    typename_list = ['2in1convertible', 'gaming', 'netbook', 'notebook', 'ultrabook', 'workstation']
    opsys_list = ['linux', 'mac', 'windows', 'other']
    cpu_list = ['amd', 'intelcorei3', 'intelcorei5', 'intelcorei7', 'other']
    gpu_list = ['amd', 'intel', 'nvidia']

    add_one_hot(feature_list, company_list, company)
    add_one_hot(feature_list, typename_list, typename)
    add_one_hot(feature_list, opsys_list, opsys)
    add_one_hot(feature_list, cpu_list, cpu)
    add_one_hot(feature_list, gpu_list, gpu)

    prediction = model.predict([feature_list])
    price = np.round(prediction[0] * 380)

    st.success(f"Estimated Laptop Price: LKR {price:,.0f}")
