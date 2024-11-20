import streamlit as st
import pandas as pd
import duckdb
import plotly.express as px

# Titre de la page
st.title("Analyse de la base de données")
st.divider()

options = ["Etape 1", "Etape 2", "Etape 3"]
selection = st.pills("Les étapes : ", options, selection_mode='single')

if "Etape 1" in selection:    
    st.image("https://raw.githubusercontent.com/Damdam86/Recommandation_film/main/images/etape1.png")
elif "Etape 2" in selection :
    st.image("https://raw.githubusercontent.com/Damdam86/Recommandation_film/main/images/etape2.png")
elif "Etape 3" in selection :
    st.image("https://raw.githubusercontent.com/Damdam86/Recommandation_film/main/images/etape3.png")
