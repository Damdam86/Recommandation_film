import streamlit as st
import pandas as pd
import duckdb
import plotly.express as px

# Titre de la page
st.title("Analyse de la base de données")
st.divider()

options = ["title.ratings", "title.akas", "title.basics", "title.crew"]
selection = st.pills("Les datas sets : ", options, selection_mode='single')

if "title.ratings" in selection:
    # Charger le fichier avec DuckDB
    st.markdown("### Analyse de title.Ratings")
    df_title_ratings = duckdb.query("SELECT * FROM '/data/title.ratings.tsv'").to_df()
    st.write("Aperçu des données:", df_title_ratings.head(5))

    # Graphique 1 : Répartition des évaluations moyennes
    st.markdown("### Répartition des Évaluations Moyennes")
    fig1 = px.histogram(df_title_ratings, x='averageRating', title="Évaluations Moyennes")
    st.plotly_chart(fig1, use_container_width=True)

    # Graphique 2 : Distribution des évaluations par groupes
    # Créer des catégories (bins) pour les groupes de notes
    bins = [0, 3, 5, 8, 10]
    labels = ['0-3', '3-5', '5-8', '8-10']
    df_title_ratings['rating_group'] = pd.cut(df_title_ratings['averageRating'], bins=bins, labels=labels, include_lowest=True)

    # Compter les occurrences de chaque groupe de notes
    grouped_counts = df_title_ratings['rating_group'].value_counts().reindex(labels).reset_index()
    grouped_counts.columns = ['rating_group', 'count']

    # Graphique en barres pour les groupes de notes
    st.markdown("### Distribution des Évaluations par Groupe")
    fig2 = px.bar(grouped_counts, x='rating_group', y='count', title="Distribution des Évaluations par Groupe")
    fig2.update_layout(xaxis_title="Groupe de Notes", yaxis_title="Nombre d'Évaluations")
    st.plotly_chart(fig2, use_container_width=True)


    st.markdown("### Nos recommandations")
    st.warning('Ne garder dans la base que les films avec une note supérieure à 5')

