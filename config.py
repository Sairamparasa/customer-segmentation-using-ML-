"""
Configuration file for Customer Segmentation Project
"""

import os

# Project paths
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(PROJECT_ROOT, 'data')
MODELS_DIR = os.path.join(PROJECT_ROOT, 'models')
NOTEBOOKS_DIR = os.path.join(PROJECT_ROOT, 'notebooks')
SRC_DIR = os.path.join(PROJECT_ROOT, 'src')

# Data files
CUSTOMER_DATA_FILE = os.path.join(DATA_DIR, 'customer_segmentation.csv')

# Model files
KMEANS_MODEL_FILE = os.path.join(MODELS_DIR, 'kmeans_model.pkl')
SCALER_MODEL_FILE = os.path.join(MODELS_DIR, 'scaler.pkl')

# Model parameters
N_CLUSTERS = 6
FEATURES = [
    'Age', 'Income', 'Total_Spending', 
    'NumWebPurchases', 'NumStorePurchases', 
    'NumWebVisitsMonth', 'Recency'
]

# App configuration
APP_TITLE = "Customer Segmentation App"
APP_DESCRIPTION = "Enter customer details to predict the segment"