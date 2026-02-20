# 📊 Listings Notebook Analysis - Lyon Airbnb Price Prediction

## 🎯 **Objective**
Built a **Random Forest Regressor** to help Airbnb users in Lyon identify optimal market prices for their listings. Users input property details through a form to receive data-driven price recommendations and remain competitive.

## 🔧 **Data Science Process Applied**

### **Data Cleaning & Preprocessing**
- Handled missing values using KNN for bedrooms data
- Cleaned price and date columns
- Standardized categorical variables
- Removed irrelevant data points

### **Feature Engineering & Analysis**
- Analyzed histograms and tested for data skewness
- Applied log and Box-Cox transformations to normalize variables
- Encoded categorical variables (Superhost, Room Type, License Type)
- Selected relevant features through correlation analysis

### **Machine Learning Implementation**
- Built Random Forest Regressor model
- Optimized model parameters using GridSearchCV
- Evaluated performance with standard metrics

### **Exploratory Data Analysis**
- Created visualizations to understand data patterns
- Analyzed feature relationships and correlations
- Examined geographic price distributions

### **Interactive Dashboard Design**
- Built Power BI dashboard for data visualization
- Demonstrated price impact when model variables change
- Created interactive insights for stakeholders

### **Web Application Development**
- Developed Streamlit app with predictive model integration
- Built user-friendly form interface for price estimation
- Enabled real-time predictions based on property characteristics

## 📈 **Project Outcomes & Deliverables**
- ✅ Clean datasets (`df_clean.csv`, `df_model.csv`) ready for machine learning
- ✅ Optimized Random Forest price prediction model
- ✅ Interactive Power BI dashboard for data visualization
- ✅ Streamlit web application for real-time price predictions

## 🛠 **Technologies Used**
- **Python**: pandas, numpy, scikit-learn
- **Machine Learning**: KNN, Random Forest, GridSearchCV  
- **Visualization**: matplotlib, seaborn, Power BI
- **Web Development**: Streamlit