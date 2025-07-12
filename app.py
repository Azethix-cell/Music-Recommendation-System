import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# --- Spotify API Credentials ---
CLIENT_ID = "f4debf1e0ddc4517a3f9f334c5490896"
CLIENT_SECRET = "91c6af3177ba45bd96d6d6f62a942ebb"

# --- Initialize Spotify client ---
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# --- Function to get album cover, preview URL, and Spotify URL ---
def get_song_album_cover_and_preview_and_url(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")
    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        album_cover_url = track["album"]["images"][0]["url"]
        preview_url = track.get("preview_url", None)
        spotify_url = track["external_urls"]["spotify"]
        return album_cover_url, preview_url, spotify_url
    else:
        return "https://i.postimg.cc/0QNxYz4V/social.png", None, "#"

# --- Recommendation function ---
def recommend(song, music_df):
    index = music_df[music_df['song'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_music_names = []
    recommended_music_posters = []
    recommended_music_previews = []
    recommended_music_urls = []
    for i in distances[1:6]:
        artist = music_df.iloc[i[0]].artist
        song_name = music_df.iloc[i[0]].song
        album_cover_url, preview_url, spotify_url = get_song_album_cover_and_preview_and_url(song_name, artist)
        recommended_music_names.append(song_name)
        recommended_music_posters.append(album_cover_url)
        recommended_music_previews.append(preview_url)
        recommended_music_urls.append(spotify_url)
    return recommended_music_names, recommended_music_posters, recommended_music_previews, recommended_music_urls

# --- Streamlit App UI ---
st.header('Music Recommender System')

music = pickle.load(open('df.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

# --- Genre & Mood Filters ---
genre_options = ["All"] + sorted(music['genre'].dropna().unique())
mood_options = ["All"] + sorted(music['mood'].dropna().unique())

selected_genre = st.selectbox("Filter by Genre", genre_options)
selected_mood = st.selectbox("Filter by Mood", mood_options)

filtered_music = music.copy()
if selected_genre != "All":
    filtered_music = filtered_music[filtered_music['genre'] == selected_genre]
if selected_mood != "All":
    filtered_music = filtered_music[filtered_music['mood'] == selected_mood]

music_list = filtered_music['song'].values

selected_song = st.selectbox(
    "Type or select a song from the dropdown",
    music_list
)

if st.button('Show Recommendation'):
    recommended_music_names, recommended_music_posters, recommended_music_previews, recommended_music_urls = recommend(selected_song, filtered_music)
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        col.text(recommended_music_names[idx])
        col.image(recommended_music_posters[idx])
        if recommended_music_previews[idx]:
            col.audio(recommended_music_previews[idx], format="audio/mp3")
        else:
            col.write("No audio preview available.")
        # Spotify Play Button
        col.markdown(
            f'<a href="{recommended_music_urls[idx]}" target="_blank">'
            f'<img src="https://img.icons8.com/color/48/000000/spotify--v1.png" width="32"/>'
            '</a>',
            unsafe_allow_html=True
        )
