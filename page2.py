import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# Titre et introduction
st.title("📽️ Projet : Recommandation de films")
st.write("L'objectif est de mettre en place un système de recommandation de films pour un cinéma qui connaît actuellement une baisse de son chiffre d'affaires.")

# Infos client / projet
st.divider()
st.markdown("## Parce que c’est votre projet !")
st.markdown("#### Votre métier")
st.write("Cinéma situé dans la Creuse")
st.markdown("#### Problématique")
st.write("Votre cinéma est actuellement en perte de vitesse avec une baisse du chiffre d'affaires.")
st.markdown("#### Besoin client")
st.write("Disposer d’un outil pour la recommandation de films et explorer des services additionnels pour relancer la croissance.")
st.markdown("### Contraintes")
st.write("Aucune donnée interne sur les goûts des clients. Utilisation initiale de données externes.")



# Livraison
st.divider()
st.markdown("### 📅 Délai de livraison")
# Utilisation de components.html pour intégrer le widget de countdown ! 
components.html(
    """
    <script src="https://cdn.logwork.com/widget/countdown.js"></script>
    <a href="https://logwork.com/countdown-hu2f" 
    class="countdown-timer" 
    data-timezone="Europe/Paris" 
    data-language="fr" 
    data-textcolor="#000000" 
    data-date="2025-01-07 14:00" 
    data-background="#000000" 
    data-digitscolor="#ffffff" 
    data-unitscolor="#000000">.</a>
    """,
    height=200  # Ajustez la hauteur selon vos besoins
)
progress_text = "Avancement du projet"
my_bar = st.progress(0.2, text=progress_text)  

# Rétroplanning 
st.divider()
st.header("📅 Rétroplanning")
st.write("Voici le rétroplanning du projet.")

retroplanning = {
    "Étape": ["Réaliser une étude de marché sur la consommation de cinéma dans la Creuse", 
              "Réaliser une étude de marché sur la consommation de cinéma dans la Creuse", 
              "Appropriation, exploration des données et nettoyage (Pandas, Matplotlib, Seaborn)", 
              "Appropriation, exploration des données et nettoyage (Pandas, Matplotlib, Seaborn)", 
              "Machine learning et recommandations (scikit-learn)",
              "Machine learning et recommandations (scikit-learn)",
              "Affinage, interface et présentation"],
    "Timing": ["Semaine 1", 
               "Semaine 2", 
               "Semaine 3", 
               "Semaine 4",
               "Semaine 5",
               "Semaine 6",
               "Semaine 7"],
    "Statut": ["✅", "✅", "🛠️", "🛠️", "📅", "📅", "📅"]
}
df_retroplanning = pd.DataFrame(retroplanning)

st.write(df_retroplanning)

# Détails du système de recommandation avec conteneur de fond et icônes
st.divider()
st.header("🔧 Détails du Système de Recommandation")
st.write("Le tableau ci-dessous présente les principales caractéristiques de notre système de recommandation.")

system_features = {
    "Caractéristique": [
        "🎯 Personnalisation",
        "🌐 Utilisation de données externes",
        "👥 Filtrage collaboratif",
        "📑 Filtrage basé sur le contenu"
    ],
    "Description": [
        "Recommandations personnalisées basées sur les préférences des utilisateurs",
        "Utilisation de données externes pour pallier l'absence de données internes",
        "Suggestions basées sur les préférences d'autres utilisateurs",
        "Recommandations basées sur les caractéristiques des films"
    ],
    "Statut": ["🛠️", "✅", "🛠️", "📅"]
}
df_system_features = pd.DataFrame(system_features)
st.write(df_system_features)