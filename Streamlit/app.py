# IMPORTAMOS LIBRERIAS
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Configuración de la página
st.set_page_config(
    page_title="Data Analysis Airbnb",
    page_icon="🏠",
    layout="centered",
    initial_sidebar_state="expanded",
)

#Usar data df_clean
df_cleaned = pd.read_csv(r'data/df_clean.csv')

#TITULO DE LA APLICACION
st.title('DATA ANALYSIS AIRBNB')

df_cleaned
