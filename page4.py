import streamlit as st
import requests


######################################## DEBUT DES FONCTIONS ####################################################

# **Définir la configuration de la page en premier !**
st.set_page_config(
    page_title="Recommandation de Film",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Clé API
api_key = "192f96229b83ef4a1fa6add55531870f"

# Récupérer la liste des films populaires
def get_movies():
    url = f"https://api.themoviedb.org/3/movie/top_rated?language=fr-FR&api_key={api_key}"
    response = requests.get(url)
    movie_data = response.json()
    movies = [{"id": movie["id"], "title": movie["title"]} for movie in movie_data.get("results", [])]
    return movies

movies_list = get_movies()

def get_movie_ba(movie_id, api_key):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?language=fr-FR&api_key={api_key}"
    response = requests.get(url)
    movie_ba = response.json()

    # Vérifie si "results" contient des données
    if "results" in movie_ba and len(movie_ba["results"]) > 0:
        for ba in movie_ba["results"]:
            # Recherche un trailer YouTube
            if ba.get("site") == "YouTube" and ba.get("type") == "Trailer":
                ba_url = f"https://www.youtube.com/watch?v={ba['key']}" # Retourne le lien du premier trailer trouvé
                return ba_url
    
    # Si aucun trailer n'est trouvé, retourne un message par défaut
    return None

# Récupérer les détails d'un film
def get_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=fr-FR&api_key={api_key}"
    response = requests.get(url)
    return response.json()

# Récupérer les informations sur l'équipe du film (crew et casting)
def get_movie_crew(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?language=fr-FR&api_key={api_key}"
    response = requests.get(url)
    return response.json()

# Extraire le réalisateur
def get_director(data_crew):
    directors = []
    for person in data_crew.get("crew", []):
        if "job" in person and person["job"] == "Director":
            if "name" in person:
                directors.append(person["name"])
    if directors:
        return ", ".join(directors)
    else:
        return "Non spécifié"
    
# Extraire les acteurs principaux
def get_actors(data_crew):
    actors = []
    cast_list = data_crew.get("cast", [])
    if cast_list:
        for cast in cast_list[:5]:  # Limiter à 5 acteurs principaux
            actor = {}
            actor["name"] = cast.get("name", None)
            actor["character"] = cast.get("character", None)
            actor["profile_path"] = cast.get("profile_path", None)
            actors.append(actor)
    return actors

def get_avis(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/reviews?language=fr-FR&page=1&api_key={api_key}"
    response = requests.get(url)
    data = response.json()
    avis_list = []
    for avis in data.get("results", []):
        avis_details = {
            "author": avis.get("author"),
            "rating": avis.get("author_details"),
            "content": avis.get("content"),
        }
        avis_list.append(avis_details)
    return avis_list

# Liste déroulante pour sélectionner un film
selected_movie_title = st.selectbox("Sélectionnez un film :",options=[movie["title"] for movie in movies_list])

# Trouver l'ID correspondant au film sélectionné
selected_movie_id = next(movie["id"] for movie in movies_list if movie["title"] == selected_movie_title)

# Charger les détails et le crew du film sélectionné
movie_data = get_movie_details(selected_movie_id)
movie_crew = get_movie_crew(selected_movie_id)

######################################## FIN DES FONCTIONS ####################################################

########################################## CSS #################################################################
st.markdown(
    """
    <style>
    .css-18e3th9 {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    .css-1d391kg {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    .circular-image {
        display: block;
        margin: 0 auto;
        border-radius: 50%;
        width: 100px;
        height: 100px;
        object-fit: cover;
    }
    .actor-container {
        text-align: center;
        margin-bottom: 30px;
    }
    .actor-name {
        font-weight: bold;
        margin-top: 10px;
    }
    .actor-role {
        font-style: italic;
        color: gray;
    }
    </style>
    """,
    unsafe_allow_html=True
)


##################################### Titre de la page#####################################
st.title(movie_data.get("title"))
st.markdown(f"**Titre original : {movie_data.get('original_title')}**")


######################################### Partie haute #####################################
# Contenu principal avec deux colonnes
col1, col2, col3 = st.columns([1, 1, 3])
image_width = 100  # Largeur de l'image en pixels

with col1:  # Affiche
    st.image(
        f"https://image.tmdb.org/t/p/original/{movie_data.get('poster_path')}",
        caption=movie_data.get("title"),
        use_container_width=True
    )

with col2:  # Informations principales
    st.markdown(f"**Date de sortie :** {movie_data.get('release_date')}")
    st.markdown(f"**Durée :** {movie_data.get('runtime')} minutes")
    #création de la liste des genres
    genres = [genre['name'] for genre in movie_data.get('genres', [])]
    st.markdown(f"**Genres :** {', '.join(genres)}")
    st.markdown(f"**Note TMDb :** ⭐ {movie_data.get('vote_average')}")
    st.markdown(f"**Nbre de votes :** 👍 {movie_data.get('vote_count')}")
    st.markdown(f"**Réalisation :** {get_director(movie_crew)}")
    st.button("Ajouter à la liste de favoris")
    st.button("Réservez votre place")

with col3:  # Résumé et détails techniques
    st.markdown("#### 📝 Résumé")
    st.write(movie_data.get("overview"))

    st.markdown("#### 📸 Casting principal :") #Affichage des 5 acteurs principaux
    actors = get_actors(movie_crew)
    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
    with col1:
        st.image(f"https://image.tmdb.org/t/p/original/{actors[0]['profile_path']}", width=image_width)
        st.markdown(actors[0]['name'])
        st.markdown(actors[0]['character'])
    with col2:
        st.image(f"https://image.tmdb.org/t/p/original/{actors[1]['profile_path']}", width=image_width)
        st.markdown(actors[1]['name'])
        st.markdown(actors[1]['character'])
    with col3:
        st.image(f"https://image.tmdb.org/t/p/original/{actors[2]['profile_path']}", width=image_width)
        st.markdown(actors[2]['name'])
        st.markdown(actors[2]['character'])
    with col4:
        st.image(f"https://image.tmdb.org/t/p/original/{actors[3]['profile_path']}", width=image_width)
        st.markdown(actors[3]['name'])
        st.markdown(actors[3]['character'])
    with col5:
        st.image(f"https://image.tmdb.org/t/p/original/{actors[4]['profile_path']}", width=image_width)
        st.markdown(actors[4]['name'])
        st.markdown(actors[4]['character'])


############################################### PARTIE BASSE ###################################################

# Nos recommandations
st.markdown("#### 📸 Nos recommandations")
col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])

with col1:  # Film 1
    st.markdown("Film 1")
    st.image(
        f"https://image.tmdb.org/t/p/original/{movie_data.get('poster_path')}",
        caption=movie_data.get("title"),
        width=image_width
    )

with col2:  # Film 2
    st.markdown("Film 2")
    st.image(
        f"https://image.tmdb.org/t/p/original/{movie_data.get('poster_path')}",
        caption=movie_data.get("title"),
        width=image_width
    )

with col3:  # Film 3
    st.markdown("Film 3")
    st.image(
        f"https://image.tmdb.org/t/p/original/{movie_data.get('poster_path')}",
        caption=movie_data.get("title"),
        width=image_width
    )

with col4:  # Film 4
    st.markdown("Film 4")
    st.image(
        f"https://image.tmdb.org/t/p/original/{movie_data.get('poster_path')}",
        caption=movie_data.get("title"),
        width=image_width
    )

with col5:  # Film 5
    st.markdown("Film 5")
    st.image(
        f"https://image.tmdb.org/t/p/original/{movie_data.get('poster_path')}",
        caption=movie_data.get("title"),
        width=image_width
    )


# Bande-annonce et avis
col1, col2, col3 = st.columns([1, 1, 3])

with col1:  # Bande annonce
    st.markdown("#### 🎥 Bande-Annonce")
    ba_url = get_movie_ba(selected_movie_id, api_key)
    st.video(ba_url)


with col2:  #colonne de séparation
    ""

with col3:  # Les avis
    st.markdown("#### 💬 Critique")
    avis_list = get_avis(selected_movie_id)
    for avis in avis_list: 
        st.markdown(f"🖊️ **Auteur :** {avis['author']}")
        st.markdown(f"⭐ **Note :** {avis['rating']}")
        st.text(f"💬 **Commentaire :** {avis['content']}")