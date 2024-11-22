import streamlit as st
import pandas as pd
import seaborn as sns
import plotly as px


# Définir la navigation entre les pages
pg = st.navigation([
        st.Page("page2.py", title="Le projet", icon="🔥"),
        st.Page("page1.py", title="L'équipe projet", icon="🤹‍♀️"),
        st.Page("page3.py", title="Analyse de la base de données", icon="📊"),
        st.Page("page4.py", title="Recommandation", icon="🎬"),
])

# Exécuter la page sélectionnée
pg.run()