# Project_Airbnb
In this project, my main goal was to develop a predictive model to estimate Airbnb listing prices in the city of Lyon by analyzing how prices are influenced by different variables, and to provide personalized recommendations to users.

Steps followed: 

1. Data Preprocessing and EDA <br/>
Certain variables were imputed with a KNN Regressor.

2. Model Preparation <br/>
Analyzed histograms of key variables. <br/>
Tested for skewness and applied logarithmic or Box-Cox transformations as needed, followed by re-evaluating histograms. <br/>
Examined variable correlations to identify potential predictors. <br/>
Encoded categorical variables such as Superhost (True/False), Room Type, and License Type. <br/>

3. Model Building <br/>
Implemented a Random Forest Regressor to build the prediction model.

4. Interactive Dashboard Design <br/>
Created a Power BI dashboard to visualize insights and demonstrate how Airbnb listing prices are affected as the variables included in our prediction model are adjusted or modified.

5. Result Presentation Application <br/>
Developed a Streamlit app to showcase the findings, incorporating the predictive model and an interactive, form-based interface. Users can input key property details, such as neighborhood, number of bedrooms, number of bathrooms, host type and other relevant characteristics, to generate an estimated listing price for the Airbnb based on the model's predictions.
  
 
## Project Configuration

### Data csv's

This project requires CSV files that are not included in the repository.
- Datasets from: [Inside Airbnb](https://insideairbnb.com/get-the-data/).

## PowerBi Summary Panel

![Captura de pantalla 2024-12-11 155915](https://github.com/user-attachments/assets/14c7c127-feb2-4ac6-bc2d-78916675462c)
![Captura de pantalla 2024-12-11 155057](https://github.com/user-attachments/assets/6f7f097e-10d9-46f9-bf03-e48c7f5bbf9c)


