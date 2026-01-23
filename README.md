# Customer Segmentation Project using K-Means

A complete customer segmentation solution using K-means clustering to identify distinct customer groups based on their purchasing behavior, demographics, and engagement patterns.

## 📁 Project Structure

```
customer_segmentation/
├── data/                           # Data files
│   └── customer_segmentation.csv   # Raw customer data (2,240 customers, 29 features)
├── notebooks/                      # Jupyter notebooks
│   └── EDA.ipynb                  # Exploratory Data Analysis & Model Training
├── models/                         # Trained models
│   ├── kmeans_model.pkl           # Trained K-means model (6 clusters)
│   └── scaler.pkl                 # Feature scaler for preprocessing
├── src/                           # Source code
│   ├── __init__.py               # Package initialization
│   └── segmentation_app.py       # Streamlit web application
├── docs/                          # Documentation
├── venv/                          # Virtual environment
├── config.py                      # Configuration settings
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation
```

## 🎯 Project Overview

This project implements customer segmentation using unsupervised machine learning to help businesses:
- Identify distinct customer groups
- Understand customer behavior patterns
- Develop targeted marketing strategies
- Improve customer retention and acquisition

## 📊 Dataset Features

### Demographics
- **Age**: Customer age (derived from birth year)
- **Education**: Education level (Graduation, PhD, Master, 2n Cycle, Basic)
- **Marital_Status**: Relationship status
- **Income**: Annual household income

### Purchase Behavior
- **Total_Spending**: Sum of all product category purchases
- **NumWebPurchases**: Number of web purchases
- **NumStorePurchases**: Number of store purchases
- **NumCatalogPurchases**: Number of catalog purchases
- **Recency**: Days since last purchase

### Engagement
- **NumWebVisitsMonth**: Monthly website visits
- **Campaign Response**: Response to marketing campaigns

## 🔧 Installation & Setup

1. **Clone the repository**
```bash
git clone <repository-url>
cd customer_segmentation
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

## 🚀 Usage

### Run the Streamlit App
```bash
cd src
streamlit run segmentation_app.py
```

### Explore the Analysis
Open `notebooks/EDA.ipynb` in Jupyter to see:
- Data exploration and visualization
- Feature engineering process
- Model training and evaluation
- Cluster analysis

## 🤖 Model Details

- **Algorithm**: K-Means Clustering
- **Number of Clusters**: 6 (determined using elbow method)
- **Features Used**: Age, Income, Total_Spending, NumWebPurchases, NumStorePurchases, NumWebVisitsMonth, Recency
- **Preprocessing**: StandardScaler for feature normalization

## 📈 Results

The model successfully segments customers into 6 distinct clusters based on their:
- Spending patterns
- Purchase frequency
- Channel preferences
- Engagement levels

## 🛠 Technologies Used

- **Python 3.8+**
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Scikit-learn**: Machine learning algorithms
- **Streamlit**: Web application framework
- **Matplotlib/Seaborn**: Data visualization
- **Joblib**: Model serialization

## 📝 Future Enhancements

- [ ] Add cluster profiling and interpretation
- [ ] Implement cluster naming based on characteristics
- [ ] Add more visualization in the web app
- [ ] Include model performance metrics
- [ ] Add data validation and error handling
- [ ] Implement A/B testing framework

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License.
