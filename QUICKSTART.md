# 🚀 Quick Start Guide

Get the Customer Segmentation app running in 3 simple steps!

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

## Step 1: Setup
```bash
python setup.py
```
This will:
- ✅ Check Python version
- ✅ Verify all files are present
- ✅ Install required packages

## Step 2: Run the App
```bash
python run_app.py
```                     
The app will automatically open in your browser at `http://localhost:8501`

## Step 3: Use the App
1. **Enter customer details** in the sidebar:
   - Age (18-100)
   - Income ($0-$200,000)
   - Total Spending ($0-$5,000)
   - Number of web/store purchases
   - Web visits per month
   - Days since last purchase

2. **Click "Predict Segment"** to get the customer cluster

3. **View the result** - you'll see which of the 6 customer segments this customer belongs to

## 📊 Explore the Analysis
Want to see how the model was built?
```bash
jupyter notebook notebooks/EDA.ipynb
```

## 🛠 Manual Setup (Alternative)
If you prefer manual setup:

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the app:**
   ```bash
   cd src
   streamlit run segmentation_app.py
   ```

## 🔧 Troubleshooting

### Common Issues:

**"Module not found" error:**
```bash
pip install -r requirements.txt
```

**"File not found" error:**
Make sure you're in the project root directory and all files are present.

**Port already in use:**
```bash
streamlit run src/segmentation_app.py --server.port 8502
```

### Need Help?
- Check the full documentation in `README.md`
- Review technical details in `docs/PROJECT_OVERVIEW.md`
- Examine the data analysis in `notebooks/EDA.ipynb`

## 🎯 What's Next?
- Explore different customer inputs to see various segments
- Analyze the clustering results in the Jupyter notebook
- Customize the model with your own data
