# IMPORTAMOS LIBRERIAS
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Configuración de la página
st.set_page_config(
    page_title="Data Analysis Airbnb",
    page_icon="🏠",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Load data
def load_data():
    data_model = pd.read_csv('df_model.csv')
    return data_model

# Load model
@st.cache(allow_output_mutation=True)
def load_model():
    model = joblib.load('random_forest_model.pkl')
    return model

# TITULO DE LA APLICACION
st.title('DATA ANALYSIS AIRBNB')

# Cargar el modelo
model = load_model()

# Formulario para ingresar nuevos datos
st.header('Ingrese los datos del nuevo listado')
accommodates = st.number_input('Capacidad de alojamiento', min_value=1, max_value=16, value=1)
bathrooms = st.number_input('Número de baños', min_value=0.5, max_value=10.0, value=1.0, step=0.5)
bedrooms = st.number_input('Número de habitaciones', min_value=0, max_value=10, value=1)
neighbourhood_cleansed = st.selectbox('Vecindario', ['Downtown', 'Uptown', 'Suburb'])
room_type = st.selectbox('Tipo de habitación', ['Entire home/apt', 'Private room', 'Shared room'])
review_scores_rating = st.slider('Puntuación de reseñas', min_value=0, max_value=100, value=80)
availability_365 = st.number_input('Disponibilidad (días al año)', min_value=0, max_value=365, value=200)

# Crear un DataFrame con los datos ingresados
new_data = pd.DataFrame({
    'accommodates': [accommodates],
    'bathrooms': [bathrooms],
    'bedrooms': [bedrooms],
    'neighbourhood_cleansed': [neighbourhood_cleansed],
    'room_type': [room_type],
    'review_scores_rating': [review_scores_rating],
    'availability_365': [availability_365]
})

# Realizar las mismas transformaciones que aplicaste a los datos de entrenamiento
new_data = pd.get_dummies(new_data)

# Asegúrate de que las columnas de new_data coincidan con las de X_train
missing_cols = set(X_train.columns) - set(new_data.columns)
for col in missing_cols:
    new_data[col] = 0
new_data = new_data[X_train.columns]

# Hacer predicciones
if st.button('Predecir precio'):
    prediction = model.predict(new_data)
    st.write(f'El precio estimado es: ${prediction[0]:.2f}')