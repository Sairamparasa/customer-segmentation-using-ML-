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
- **Identify distinct customer groups** based on behavior and demographics
- **Understand customer behavior patterns** across different segments
- **Develop targeted marketing strategies** for each customer segment
- **Improve customer retention and acquisition** through personalized approaches
- **Optimize resource allocation** by focusing on high-value segments
- **Enhance customer experience** through segment-specific offerings

### Business Applications
- **Marketing Campaigns**: Target specific segments with relevant offers
- **Product Development**: Design products for different customer needs
- **Pricing Strategy**: Implement segment-based pricing models
- **Customer Service**: Provide personalized support based on segment
- **Inventory Management**: Stock products based on segment preferences
- **Cross-selling/Up-selling**: Recommend products within segment patterns

### Data-Driven Insights
Our analysis reveals:
- **Customer Diversity**: 6 distinct behavioral segments identified
- **Spending Patterns**: Wine purchases dominate high-value segments
- **Channel Preferences**: Clear digital vs. traditional shopping divide
- **Engagement Levels**: Varying website interaction patterns
- **Campaign Effectiveness**: Segment-specific response rates vary significantly

## 📊 Dataset Overview

### Data Source & Size
- **Dataset**: Customer transaction and demographic data from a retail company
- **Records**: 2,240 customers (after cleaning: 2,216 customers)
- **Features**: 29 original features + 4 engineered features
- **Time Period**: Customer data from 2012-2014
- **Data Quality**: 24 records with missing income values were removed (1.1% missing data)     

### Raw Data Features (29 columns)

#### 🏷️ Customer Identification
- **ID**: Unique customer identifier
- **Year_Birth**: Customer's birth year (1893-1996)
- **Dt_Customer**: Date when customer enrolled with the company

#### 👥 Demographics
- **Education**: Education level
  - Graduation (1,116 customers - 50.4%)
  - PhD (481 customers - 21.7%)
  - Master (365 customers - 16.5%)
  - 2n Cycle (200 customers - 9.0%)
  - Basic (54 customers - 2.4%)
- **Marital_Status**: Relationship status
  - Married (857 customers - 38.7%)
  - Together (573 customers - 25.9%)
  - Single (471 customers - 21.3%)
  - Divorced (232 customers - 10.5%)
  - Widow (76 customers - 3.4%)
  - Others: Alone, Absurd, YOLO (7 customers - 0.3%)
- **Income**: Annual household income ($1,730 - $666,666, avg: $52,247)

#### 👨‍👩‍👧‍👦 Family Composition
- **Kidhome**: Number of children at home (0-2)
- **Teenhome**: Number of teenagers at home (0-2)

#### 🛒 Purchase Behavior by Product Category
- **MntWines**: Amount spent on wine products ($0-$1,493, avg: $305)
- **MntFruits**: Amount spent on fruits ($0-$199, avg: $26)
- **MntMeatProducts**: Amount spent on meat ($0-$1,725, avg: $167)
- **MntFishProducts**: Amount spent on fish ($0-$259, avg: $38)
- **MntSweetProducts**: Amount spent on sweets ($0-$262, avg: $27)
- **MntGoldProds**: Amount spent on gold products ($0-$362, avg: $44)

#### 🛍️ Purchase Channels & Frequency
- **NumDealsPurchases**: Purchases made with discount (0-15, avg: 2.3)
- **NumWebPurchases**: Purchases made through website (0-27, avg: 4.1)
- **NumCatalogPurchases**: Purchases made through catalog (0-28, avg: 2.7)
- **NumStorePurchases**: Purchases made in physical stores (0-13, avg: 5.8)

#### 📱 Digital Engagement
- **NumWebVisitsMonth**: Website visits per month (0-20, avg: 5.3)
- **Recency**: Days since last purchase (0-99, avg: 49)

#### 📧 Marketing Campaign Response
- **AcceptedCmp1**: Accepted 1st campaign (0/1) - 6.4% acceptance rate
- **AcceptedCmp2**: Accepted 2nd campaign (0/1) - 1.4% acceptance rate
- **AcceptedCmp3**: Accepted 3rd campaign (0/1) - 7.4% acceptance rate
- **AcceptedCmp4**: Accepted 4th campaign (0/1) - 7.4% acceptance rate
- **AcceptedCmp5**: Accepted 5th campaign (0/1) - 7.3% acceptance rate
- **Response**: Accepted last campaign (0/1) - 15.0% acceptance rate

#### 🎯 Customer Service
- **Complain**: Customer complained in last 2 years (0/1) - 0.9% complaint rate

#### 📊 Business Metrics
- **Z_CostContact**: Cost of contacting customer (constant: 3)
- **Z_Revenue**: Revenue from customer (constant: 11)

### Engineered Features (4 additional columns)

#### 🔧 Feature Engineering Process
During data preprocessing, we created these derived features :

- **Age**: Calculated as (2026 - Year_Birth)
  - Range: 30-133 years, Average: 57.2 years
  - Most customers are middle-aged (50-70 years)

- **Total_Children**: Sum of Kidhome + Teenhome
  - Range: 0-4 children, Average: 0.9 children
  - 42% have no children, 58% have 1+ children

- **Total_Spending**: Sum of all product category spending
  - Range: $5-$2,525, Average: $606
  - Represents overall customer value

- **Customer_Since**: Days since customer enrollment
  - Calculated from Dt_Customer to present date   
  - Shows customer tenure and loyalty

### Data Quality & Preprocessing

#### ✅ Data Cleaning Steps
1. **Missing Values**: Removed 24 records (1.1%) with missing Income
2. **Date Conversion**: Converted Dt_Customer to datetime format
3. **Outlier Analysis**: Identified but retained high-income customers (business decision)
4. **Feature Scaling**: Applied StandardScaler for clustering algorithm

#### 📈 Key Data Insights
- **Customer Diversity**: Wide range of demographics and spending patterns
- **Spending Distribution**: Right-skewed with some high-value customers
- **Channel Preference**: Store purchases > Web purchases > Catalog purchases
- **Campaign Effectiveness**: Low overall response rates (1.4%-15.0%)
- **Product Preferences**: Wine is the highest spending category

#### 🎯 Features Selected for Clustering
From 33 total features, we selected 7 key features for the K-means model:
1. **Age** - Demographic segmentation
2. **Income** - Economic capacity
3. **Total_Spending** - Customer value
4. **NumWebPurchases** - Digital engagement
5. **NumStorePurchases** - Physical store preference
6. **NumWebVisitsMonth** - Online activity level
7. **Recency** - Purchase recency behavior

These features were chosen because they:
- Represent different aspects of customer behavior
- Have good variance across the dataset
- Are business-relevant for segmentation strategy
- Show clear clustering patterns in exploratory analysis

### Data Usage & Privacy
- **Data Source**: Anonymized retail customer data (2012-2014)
- **Privacy**: No personally identifiable information (PII) included
- **Compliance**: Data usage follows privacy best practices
- **Purpose**: Educational and demonstration purposes only
- **Anonymization**: Customer IDs are randomized, no real customer data exposed

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

### Algorithm & Configuration
- **Algorithm**: K-Means Clustering (unsupervised learning)
- **Number of Clusters**: 6 (optimal number determined using elbow method)
- **Initialization**: K-means++ for better convergence
- **Max Iterations**: 300 (default scikit-learn setting)
- **Random State**: Fixed for reproducible results

### Feature Selection & Preprocessing
- **Selected Features (7)**: Age, Income, Total_Spending, NumWebPurchases, NumStorePurchases, NumWebVisitsMonth, Recency
- **Feature Scaling**: StandardScaler (mean=0, std=1) applied to all features
- **Rationale**: These features capture different dimensions of customer behavior:
  - **Demographic**: Age
  - **Economic**: Income  
  - **Value**: Total_Spending
  - **Channel Preference**: Web vs Store purchases
  - **Engagement**: Web visits frequency
  - **Recency**: Purchase timing behavior

### Model Performance & Validation
- **Elbow Method**: Used to determine optimal number of clusters (k=6)
- **Silhouette Analysis**: Validated cluster quality and separation
- **Inertia**: Within-cluster sum of squares minimized
- **Convergence**: Model converged successfully in all training runs

### Cluster Characteristics
The 6 clusters represent distinct customer segments:
- **High-Value Customers**: High income, high spending
- **Digital Natives**: Prefer online channels, frequent web visits
- **Traditional Shoppers**: Prefer in-store purchases
- **Occasional Buyers**: Low frequency, high recency
- **Budget Conscious**: Lower income, moderate spending
- **Engaged Loyalists**: Regular purchases, low recency

*Note: Detailed cluster profiling available in the EDA notebook*

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
