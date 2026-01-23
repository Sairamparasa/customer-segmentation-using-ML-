import streamlit as st
import pandas as pd
import numpy as np
import joblib
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import KMEANS_MODEL_FILE, SCALER_MODEL_FILE, APP_TITLE, APP_DESCRIPTION

# Load models
kmeans = joblib.load(KMEANS_MODEL_FILE)
scaler = joblib.load(SCALER_MODEL_FILE)

st.title(APP_TITLE)
st.write(APP_DESCRIPTION)

age = st.number_input('Age',min_value=18,max_value = 100,value=35)
income=st.number_input('Income',min_value=0,max_value=200000,value=50000)
total_spending=st.number_input('Total Spending (sum of purchases)', min_value=0,max_value=5000,value=1000)
num_web_purchases=st.number_input('Number of Web Purchases',min_value = 0,max_value =100,value=10 )
num_store_purchases=st.number_input('Number of Store Purchases',min_value=0,max_value=100,value=10)
num_web_visits=st.number_input('Number of Web Visits per Month',min_value = 0,max_value= 100,value=10)
recency= st.number_input('Recency (days since last purchase)',min_value=0,max_value=365,value=30)


input_data = pd.DataFrame({
    'Age':[age],
    'Income':[income],
    'Total_Spending':[total_spending],
    'NumWebPurchases':[num_web_purchases],
    'NumStorePurchases':[num_store_purchases],
    'NumWebVisitsMonth':[num_web_visits],
    'Recency':[recency]
})

input_scaled = scaler.transform(input_data)

if st.button('Predict Segment'):

    cluster = kmeans.predict(input_scaled)[0]

    st.success(f'Predicted Segment : Cluster {cluster}')

