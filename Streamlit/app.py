# IMPORTAMOS LIBRERIAS
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
import warnings 
warnings.filterwarnings('ignore')
import seaborn as sns

#Configuración de la página
st.set_page_config(
    page_title="Data Analysis Airbnb",
    page_icon="🏠",
    layout="centered",
    initial_sidebar_state="expanded",
)






#Cargar los datos

df_cleaned = pd.read_csv(r'data/df_clean.csv')
#Poner mayusculas a las columnas
df_cleaned.columns = df_cleaned.columns.str.upper()

#Agregar otro dataframe
df_model = pd.read_csv(r'data/df_model.csv')




# Crear un menú de páginas usando selectbox
page = st.sidebar.selectbox('Selecciona una página', ["Portada",'Introducción', 'Análisis de Datos', 'Visualización', 'Predicción'])

# Mostrar contenido basado en la selección
if page == 'Portada':
    st.markdown("<h1 style='text-align: center;'>Data Analysis Airbnb</h1>", unsafe_allow_html=True)
elif page == 'Introducción':
    st.markdown('<h1 style="text-align: center;">Introducción</h1>', unsafe_allow_html=True)
elif page == 'Análisis de Datos':
    st.write('Aquí se realizará el análisis de datos.')
elif page == 'Visualización':
    st.write('Aquí se mostrarán las visualizaciones.')
elif page == 'Predicción':
    st.write('Aquí se realizará la predicción.')

if page == 'Portada':
   

    # Subtitulo
    st.markdown("<h2 style='text-align: center;'>By Germán Domínguez</h2>", unsafe_allow_html=True)

    st.sidebar.title('Menú')
    st.image(r'Img\_8b5b6311-2530-4d08-8ce6-c8220c655f1e.jpg', use_column_width=True)



# PAGINA DE INTRODUCCION

if page == 'Introducción':
    st.write("El objetivo es explorar cómo varían los precios de las publicaciones de Airbnb en Lyon en función de diferentes características como ubicación, tipo de alojamiento, y otros factores importantes.")
    st.markdown("### Variables a considerar:")

    #Cols
    col1, col2, col3 = st.columns([1, 2, 3])

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("#### Vivienda")
        #Mostramos una tabla de las variables
        columns_vivienda = ['Bathrooms', 'Bedrooms', 'Room_type', 'Accomodates', 'Amenities_count',"Review_score_raing"]
        for column in columns_vivienda:
            st.markdown(f"- {column}")

    with col2:
        st.markdown("#### Operación")
        #Mostramos una tabla de las variables
        columns_otras = ["Price","Minimum_nights","Maximum_nights","Availability_365"]
        for column in columns_otras:
            st.markdown(f"- {column}")

    with col3:
        st.markdown("#### Ubicación")
        #Mostramos una tabla de las variables
        columns_ubicacion = ['Latitude', 'Longitude', 'Neighbourhood_cleansed']
        for column in columns_ubicacion:
            st.markdown(f"- {column}")







# PAGINA DE ANALISIS DE DATOS

if page == 'Análisis de Datos':
    
    #tabs 
    tab1, tab2, tab3 = st.tabs(['Datos', 'Análisis', 'Visualización'])

    #with tab3:
       # st.write("Visualización de datos")
        #fig, ax = plt.subplots()
        #sns.countplot(data=df_cleaned, x="id", ax=ax)
        #st.pyplot(fig)





if page == "Predicción":

    from sklearn.ensemble import RandomForestRegressor

#Cargar modelo
@st.cache(allow_output_mutation=True)
def load_model():
    model = joblib.load(r'Data\random_forest_model.pkl')
    return model   

# Cargar el modelo entrenado
best_forest = RandomForestRegressor(max_features=10, n_estimators=500)
best_forest = load_model()

# Título de la aplicación
st.title("Predicción de Precio de Airbnb")

# Crear entradas para que el usuario ingrese los valores
accommodates = st.number_input('Número de huéspedes', min_value=1, max_value=16, value=2)
bathrooms = st.number_input('Número de baños', min_value=1, max_value=10, value=1)
bedrooms = st.number_input('Número de habitaciones', min_value=1, max_value=10, value=1)
amenities_count = st.number_input('Número de comodidades', min_value=1, max_value=100, value=10)
minimum_nights = st.number_input('Número mínimo de noches', min_value=1, max_value=365, value=2)
maximum_nights = st.number_input('Número máximo de noches', min_value=1, max_value=365, value=30)
availability_365 = st.number_input('Disponibilidad en el año', min_value=0, max_value=365, value=365)
number_of_reviews_ltm = st.number_input('Número de reseñas en el último mes', min_value=0, max_value=100, value=0)
review_scores_rating = st.number_input('Calificación de reseñas', min_value=0.0, max_value=5.0, value=4.5)
review_scores_rating = st.slider('Calificación de reseñas', min_value=0.0, max_value=5.0, value=4.5, step=0.1)
host_is_superhost = st.selectbox('¿Es superhost?', ['Sí', 'No'])
room_type = st.selectbox('Tipo de habitación', ['Entire home/apt', 'Hotel room', 'Private room', 'Shared room'])
license_status = st.selectbox('Estado de la licencia', ['Licensed', 'Unlicensed', 'Exempt', 'Mobility lease only'])
neighbourhood_cleansed = st.selectbox('Barrio', ["1er Arrondissement", "2e Arrondissement", "3e Arrondissement", "4e Arrondissement", "5e Arrondissement", "6e Arrondissement", "7e Arrondissement", "8e Arrondissement", "9e Arrondissement"])

# Convertir las entradas a un DataFrame
nueva_publicacion = pd.DataFrame({
    'accommodates': [np.log1p(accommodates)],
    'bathrooms': [np.log1p(bathrooms + 1)],
    'amenities_count': [amenities_count],
    'minimum_nights': [minimum_nights],
    'maximum_nights': [maximum_nights],
    'availability_365': [availability_365],
    'number_of_reviews_ltm': [np.log1p(number_of_reviews_ltm)],
    'review_scores_rating': [review_scores_rating],
    'bedrooms': [np.log1p(bedrooms)],
    'host_is_superhost_false': [1 if host_is_superhost == 'No' else 0],
    'host_is_superhost_true': [1 if host_is_superhost == 'Sí' else 0],
    'Entire home/apt': [1 if room_type == 'Entire home/apt' else 0],
    'Hotel room': [1 if room_type == 'Hotel room' else 0],
    'Private room': [1 if room_type == 'Private room' else 0],
    'Shared room': [1 if room_type == 'Shared room' else 0],
    'Exempt': [1 if license_status == 'Exempt' else 0],
    'Mobility lease only': [1 if license_status == 'Mobility lease only' else 0],
    'Unlicensed': [1 if license_status == 'Unlicensed' else 0],
    'licensed': [1 if license_status == 'licensed' else 0],
    '1er Arrondissement': [1 if neighbourhood_cleansed == '1er Arrondissement' else 0],
    '2e Arrondissement': [1 if neighbourhood_cleansed == '2e Arrondissement' else 0],
    '3e Arrondissement': [1 if neighbourhood_cleansed == '3e Arrondissement' else 0],
    '4e Arrondissement': [1 if neighbourhood_cleansed == '4e Arrondissement' else 0],
    '5e Arrondissement': [1 if neighbourhood_cleansed == '5e Arrondissement' else 0],
    '6e Arrondissement': [1 if neighbourhood_cleansed == '6e Arrondissement' else 0],
    '7e Arrondissement': [1 if neighbourhood_cleansed == '7e Arrondissement' else 0],
    '8e Arrondissement': [1 if neighbourhood_cleansed == '8e Arrondissement' else 0],
    '9e Arrondissement': [1 if neighbourhood_cleansed == '9e Arrondissement' else 0],
})

# Realizar la predicción
prediccion_precio = best_forest.predict(nueva_publicacion)

# Deshacer la transformación logarítmica para obtener el precio en la escala original
precio_original = np.expm1(prediccion_precio)

# Botón para realizar la predicción
if st.button('Predecir Precio'):
    # Realizar la predicción
    prediccion_precio = best_forest.predict(nueva_publicacion)
    
    # Deshacer la transformación logarítmica para obtener el precio en la escala original
    precio_original = np.expm1(prediccion_precio)
    
    # Mostrar el resultado
    st.write(f"El precio estimado para la nueva publicación es: ${precio_original[0]:.2f}")