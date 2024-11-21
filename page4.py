
import streamlit as st

# Titre de la page
st.title("Vol à haut risque")
st.markdown("**Titre original : Flight Risk**")

# Détails principaux
col1, col2 = st.columns([1, 2])
with col1:
    st.image("https://raw.githubusercontent.com/<username>/<repository>/main/images/flight_risk_poster.jpg", caption="Flight Risk Poster")

with col2:
    st.markdown("### **2024 • 1h31min**")
    st.markdown("**Genres :** Action, Crime, Drama, Thriller")
    st.markdown("**Note IMDb :** ⭐ 7.9/10 (93 votes)")
    st.markdown("**Popularité :** 🔥 792 • 👍 310")
    st.button("Ajouter à la liste de favoris")
    st.markdown("Sortie prévue : **22 janvier 2025**")

# Bande-Annonce
st.markdown("### 🎥 Bande-Annonce")
st.video("https://www.youtube.com/embed/xyz")  # Remplacez par l'URL YouTube intégrée

# Résumé
st.markdown("### 📝 Résumé")
st.write("""
Un marshal de l'air transportant un fugitif à travers les étendues sauvages de l'Alaska à bord d'un petit avion se retrouve piégé 
lorsqu'elle soupçonne que le pilote n'est pas celui qu'il prétend être.
""")

# Détails techniques
st.markdown("### 🎬 Détails Techniques")
st.markdown("- **Réalisation :** [Mel Gibson](https://www.imdb.com/name/nm0000154/)")
st.markdown("- **Scénario :** Jared Rosenberg")
st.markdown("- **Casting principal :** Mark Wahlberg, Michelle Dockery, Topher Grace")

# Photos
st.markdown("### 📸 Photos")
cols = st.columns(4)
image_urls = [
    "https://raw.githubusercontent.com/<username>/<repository>/main/images/photo1.jpg",
    "https://raw.githubusercontent.com/<username>/<repository>/main/images/photo2.jpg",
    "https://raw.githubusercontent.com/<username>/<repository>/main/images/photo3.jpg",
    "https://raw.githubusercontent.com/<username>/<repository>/main/images/photo4.jpg"
]
for i, col in enumerate(cols):
    if i < len(image_urls):
        col.image(image_urls[i], use_column_width=True)

# Avis
st.markdown("### 💬 Avis")
st.info("2 avis des critiques. À découvrir bientôt.")

