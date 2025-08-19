# IMPORTAMOS LIBRERIAS
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
import warnings 
warnings.filterwarnings('ignore')
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
import os
import pathlib

#Configuración de la página
st.set_page_config(
    page_title="Data Analysis Airbnb",
    page_icon="🏠",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Configurar rutas de manera robusta para deploy
current_dir = pathlib.Path(__file__).parent
data_dir = current_dir / "Data"
img_dir = current_dir / "Img"

# Ruta del modelo - probar múltiples ubicaciones
model_paths = [
    current_dir / "random_forest_model.pkl",                    # Raíz del proyecto (para deploy)
    current_dir / "Streamlit" / "random_forest_model.pkl",      # Ruta original
]

# Cargar datos con rutas robustas
try:
    df_cleaned = pd.read_csv(data_dir / 'df_clean.csv')
    df_cleaned.columns = df_cleaned.columns.str.upper()
    df_model = pd.read_csv(data_dir / 'df_model.csv')
except FileNotFoundError as e:
    st.error(f"Error cargando datos: {e}")
    st.stop()

page = st.sidebar.selectbox('Menú', ["Portada",'Introducción', 'Análisis de Datos', 'Panel Power BI', 'Predicción'])

if page == 'Portada':
    # Imagen con subtítulo/caption usando ruta robusta
    image_path = img_dir / '_8b5b6311-2530-4d08-8ce6-c8220c655f1e.jpg'
    if image_path.exists():
        st.image(str(image_path), caption='Airbnb Project', width=600)
    else:
        st.warning("Imagen no encontrada")
    
    # Línea separadora
    st.markdown("---")
    
elif page == 'Introducción':
    pass
elif page == 'Análisis de Datos':
    pass
elif page == 'Panel Power BI':
    pass
elif page == 'Predicción':
    pass

# PAGINA DE INTRODUCCION
if page == 'Introducción':
    st.write("El objetivo principal es realizar un análisis de datos de las publicacciones de Airbbn en Lyon y desarrollar un modelo de predicción que me permita recomendar a los usuarios un precio de publicación de sus viviendas.")
    st.markdown("### Variables a considerar:")

    #Cols
    col1, col2, col3 = st.columns([1, 2, 3])

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("#### Vivienda")
        #Mostramos una tabla de las variables
        columns_vivienda = ['Bathrooms', 'Bedrooms', 'Room Type', 'Accomodates', 'Amenities',"Review Score Raing"]
        for column in columns_vivienda:
            st.markdown(f"- {column}")

    with col2:
        st.markdown("#### Operación")
        #Mostramos una tabla de las variables
        columns_otras = ["Minimum_nights","Maximum_nights","Availability_365"]
        for column in columns_otras:
            st.markdown(f"- {column}")

    with col3:
        st.markdown("#### Ubicación")
        #Mostramos una tabla de las variables
        columns_ubicacion = ['Neighbourhood']
        for column in columns_ubicacion:
            st.markdown(f"- {column}")

# PAGINA DE ANALISIS DE DATOS
if page == 'Análisis de Datos':
    #tabs 
    tab1, tab2, tab3, tab4 = st.tabs(['Distritos', 'Room Type',"Características vivienda", 'License'])

# PREDICCIÓN
if page == 'Predicción':
    from sklearn.ensemble import RandomForestRegressor

    #Cargar modelo
    @st.cache_resource
    def load_model():
        # Probar diferentes rutas hasta encontrar el modelo
        for model_path in model_paths:
            if model_path.exists():
                model = joblib.load(str(model_path))
                return model
        
        # Si no se encuentra el modelo, mostrar error
        st.error("No se pudo encontrar el archivo del modelo. Asegúrate de que 'random_forest_model.pkl' esté disponible.")
        return None

    # Cargar el modelo entrenado
    best_forest = load_model()
    if best_forest is None:
        st.stop()

    # Título de la aplicación
    st.title("Predicción de Ingresos")
    st.markdown("#### Predicción de precio e ingresos potenciales para una nueva publicación en Airbnb considerando las características de la vivienda y una tasa de ocupación anual.")

    # Crear entradas para que el usuario ingrese los valores
    accommodates = st.number_input('Número de huéspedes', min_value=1, max_value=16, value=2)
    bathrooms = st.number_input('Número de baños', min_value=1, max_value=10, value=1)
    bedrooms = st.number_input('Número de habitaciones', min_value=1, max_value=10, value=1)
    amenities_count = st.number_input('Número de comodidades', min_value=1, max_value=100, value=10)
    minimum_nights = st.number_input('Número mínimo de noches', min_value=1, max_value=365, value=2)
    maximum_nights = st.number_input('Número máximo de noches', min_value=1, max_value=365, value=30)
    availability_365 = st.number_input('Disponibilidad en el año', min_value=0, max_value=365, value=365)
    number_of_reviews_ltm = st.number_input('Número de reseñas en el último mes', min_value=0, max_value=100, value=0)
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
        'Licensed': [1 if license_status == 'Licensed' else 0],
        'Unlicensed': [1 if license_status == 'Unlicensed' else 0],
        'Exempt': [1 if license_status == 'Exempt' else 0],
        'Mobility lease only': [1 if license_status == 'Mobility lease only' else 0],
        '1er Arrondissement': [1 if neighbourhood_cleansed == '1er Arrondissement' else 0],
        '2e Arrondissement': [1 if neighbourhood_cleansed == '2e Arrondissement' else 0],
        '3e Arrondissement': [1 if neighbourhood_cleansed == '3e Arrondissement' else 0],
        '4e Arrondissement': [1 if neighbourhood_cleansed == '4e Arrondissement' else 0],
        '5e Arrondissement': [1 if neighbourhood_cleansed == '5e Arrondissement' else 0],
        '6e Arrondissement': [1 if neighbourhood_cleansed == '6e Arrondissement' else 0],
        '7e Arrondissement': [1 if neighbourhood_cleansed == '7e Arrondissement' else 0],
        '8e Arrondissement': [1 if neighbourhood_cleansed == '8e Arrondissement' else 0],
        '9e Arrondissement': [1 if neighbourhood_cleansed == '9e Arrondissement' else 0]
    })

    # Inicializar session_state para mantener los resultados
    if 'precio_predicho' not in st.session_state:
        st.session_state.precio_predicho = None
    if 'ingresos_calculados' not in st.session_state:
        st.session_state.ingresos_calculados = None

    # Realizar predicción inicial para cálculos
    prediccion_precio = best_forest.predict(nueva_publicacion)
    precio_original = np.expm1(prediccion_precio)

    # Botón para realizar la predicción
    if st.button('Predecir Precio'):
        # Guardar el precio en session_state
        st.session_state.precio_predicho = precio_original[0]

    # Mostrar resultado de predicción si existe
    if st.session_state.precio_predicho is not None:
        st.success(f"💰 **Precio recomendado de publicación: €{st.session_state.precio_predicho:.2f} al día**")

    # Calcular ingresos según tasa de ocupación
    tasa_ocupacion = st.slider('Tasa de ocupación anual', min_value=0.0, max_value=100.0, value=50.0, step=0.1)

    # Botón para calcular ingresos estimados
    if st.button('Calcular Ingresos Estimados'):
        ingresos = precio_original[0] * tasa_ocupacion / 100 * 365
        ingresos = ingresos.round(2)
        st.session_state.ingresos_calculados = {
            'valor': ingresos,
            'tasa': tasa_ocupacion
        }

    # Mostrar resultado de ingresos si existe
    if st.session_state.ingresos_calculados is not None:
        st.success(f"📈 **Ingresos estimados para una tasa de ocupación del {st.session_state.ingresos_calculados['tasa']:.1f}% anual: €{st.session_state.ingresos_calculados['valor']:.2f}**")
