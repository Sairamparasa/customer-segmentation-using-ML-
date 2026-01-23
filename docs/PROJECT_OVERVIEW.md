# Customer Segmentation Project - Technical Overview

## Project Architecture

This customer segmentation project follows a modular architecture with clear separation of concerns:

### Data Layer (`data/`)
- **Raw Data**: Customer transaction and demographic data
- **Format**: CSV with 2,240 customers and 29 features
- **Size**: ~500KB

### Analysis Layer (`notebooks/`)
- **EDA.ipynb**: Complete exploratory data analysis
- **Data preprocessing and feature engineering**
- **Model training and evaluation**
- **Visualization and insights**

### Model Layer (`models/`)
- **kmeans_model.pkl**: Trained K-means clustering model
- **scaler.pkl**: StandardScaler for feature normalization
- **Serialized using joblib for efficient loading**

### Application Layer (`src/`)
- **segmentation_app.py**: Streamlit web application
- **Interactive interface for real-time predictions**
- **User-friendly input forms and result display**

## Data Pipeline

```
Raw Data → Data Cleaning → Feature Engineering → Scaling → K-Means → Clusters
```

### 1. Data Cleaning
- Removed 24 rows with missing income values
- Converted date formats
- Handled categorical variables

### 2. Feature Engineering
- **Age**: Calculated from birth year (2026 - Year_Birth)
- **Total_Children**: Sum of kids and teens at home
- **Total_Spending**: Sum across all product categories
- **Customer_since**: Days since customer registration

### 3. Feature Selection
Selected 7 key features for clustering:
- Age (demographic)
- Income (economic)
- Total_Spending (behavior)
- NumWebPurchases (channel preference)
- NumStorePurchases (channel preference)
- NumWebVisitsMonth (engagement)
- Recency (activity)

### 4. Model Training
- **Algorithm**: K-Means clustering
- **Clusters**: 6 (determined via elbow method)
- **Preprocessing**: StandardScaler normalization
- **Validation**: Silhouette analysis

## Cluster Characteristics

The model identifies 6 distinct customer segments:

### Cluster Analysis Framework
Each cluster can be analyzed across dimensions:
- **Demographics**: Age, income, family status
- **Spending**: Total amount, product preferences
- **Behavior**: Purchase frequency, channel usage
- **Engagement**: Website visits, campaign response

## Technical Specifications

### Dependencies
- **Core**: Python 3.8+, pandas, numpy
- **ML**: scikit-learn, joblib
- **Visualization**: matplotlib, seaborn
- **Web App**: streamlit

### Performance
- **Training Time**: < 1 minute on standard hardware
- **Prediction Time**: < 100ms per customer
- **Memory Usage**: < 50MB for loaded models

### Scalability Considerations
- **Data Size**: Current implementation handles up to 100K customers
- **Features**: Can accommodate additional features with retraining
- **Real-time**: Suitable for real-time prediction APIs

## Deployment Options

### Local Development
```bash
python run_app.py
```

### Production Deployment
- **Streamlit Cloud**: Direct deployment from GitHub
- **Docker**: Containerized deployment
- **Cloud Platforms**: AWS, GCP, Azure compatible

## Model Maintenance

### Retraining Triggers
- New customer data (monthly/quarterly)
- Significant business changes
- Model performance degradation

### Monitoring Metrics
- Cluster stability over time
- Prediction confidence scores
- Business KPI alignment

## Future Enhancements

### Technical Improvements
- **Model Ensemble**: Combine multiple clustering algorithms
- **Feature Automation**: Automated feature engineering
- **Real-time Pipeline**: Streaming data processing

### Business Features
- **Cluster Profiling**: Detailed segment descriptions
- **Recommendation Engine**: Product recommendations per cluster
- **Campaign Optimization**: Targeted marketing strategies

## Security & Privacy

### Data Protection
- No personally identifiable information stored
- Aggregated analytics only
- GDPR compliance considerations

### Model Security
- Input validation and sanitization
- Rate limiting for API endpoints
- Model versioning and rollback capabilities