# 📊 Listings Notebook Analysis - Lyon Airbnb Price Prediction

## 🎯 **Objective**
Built a **Random Forest Regressor** to predict optimal Airbnb listing prices in Lyon through data cleaning, feature engineering, and machine learning techniques.

## 🔧 **Data Science Process Applied**

### **Data Cleaning & Preprocessing**
- **Missing Value Handling**: Applied KNN Regressor to impute missing `bedrooms` values
- **Data Type Conversion**: Cleaned price strings and formatted date columns
- **Categorical Data Processing**: Standardized license categories
- **Data Quality**: Strategic handling of null values based on feature importance

### **Feature Engineering & Analysis**
- **Statistical Analysis**: Examined data distribution and skewness
- **Data Transformation**: Applied log transformation to normalize price variable
- **Categorical Encoding**: Used one-hot encoding for neighborhood features
- **Feature Selection**: Analyzed correlations to identify relevant predictors

### **Machine Learning Implementation**
- **Model Selection**: Implemented Random Forest Regressor
- **Model Optimization**: Used GridSearchCV to find best parameters
  - Tested different `n_estimators` and `max_features` values
- **Model Evaluation**: Applied train/test split methodology
- **Performance Assessment**: Calculated MAE and RMSE metrics

### **Exploratory Data Analysis**
- **Data Visualization**: Created histograms and distribution plots
- **Correlation Analysis**: Generated heatmaps to understand feature relationships
- **Geographic Analysis**: Plotted price variations by location coordinates
- **Data Distribution**: Assessed normality and applied appropriate transformations

## 📈 **Project Outcomes**
- ✅ Successfully handled missing data using KNN imputation approach
- ✅ Processed categorical variables for machine learning compatibility
- ✅ Built and optimized Random Forest model using GridSearchCV
- ✅ Generated clean dataset ready for price prediction applications
- ✅ Created foundation for **Streamlit web application**

## 🛠 **Technologies Used**
- **Python**: pandas, numpy, scikit-learn
- **Machine Learning**: KNN, Random Forest, GridSearchCV
- **Visualization**: matplotlib, seaborn
- **Statistical Analysis**: scipy.stats, skewness testing
- **Data Engineering**: Feature scaling, encoding, transformation

## 📊 **Final Deliverables**
- `df_clean.csv`: Processed dataset with handled missing values
- `df_model.csv`: Feature-ready data for machine learning
- Trained Random Forest model with optimized parameters
- Data analysis insights and visualizations