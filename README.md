# Music-Recommendation-System
🔊 Project Description: Music Recommendation System This project is a content-based music recommendation system built using natural language processing and machine learning. It analyzes the lyrics of songs to recommend similar music tracks.  

📌 How It Works:
It uses the lyrics of songs to compute textual similarity.

Upon entering a song name, it finds similar songs based on cosine similarity between vectorized lyrics.

The system is served through a web interface using Flask.

🔧 Tech Stack Overview
🧠 Machine Learning / Model Training
Used in: Model Training.ipynb

Python (Jupyter Notebook): For data preprocessing and model training.

Pandas: To handle and manipulate tabular music dataset.

Scikit-learn: For building the similarity matrix using techniques like cosine_similarity.

Pickle: To save trained models and data (df.pkl, similarity.pkl) for later use in the app.

🎧 Spotify API Integration
Used in: app.py

Spotipy: Python library to access the Spotify Web API.

Used to get album cover, preview audio, and Spotify URLs for tracks.

🖥️ Web Application
Used in: app.py

Streamlit: Used to build an interactive UI for the recommender system.

Dropdowns for genre/mood filtering

Display of recommendations with images, audio previews, and Spotify links

🗃️ Data Format
DataFrame (df.pkl): Likely includes columns like song, artist, genre, mood, etc.

Similarity Matrix (similarity.pkl): A precomputed similarity score matrix for content-based recommendations.
🔑 Key Components / Features
1. Data Preprocessing:
Lyrics cleaned and vectorized using TF-IDF Vectorizer.

Dataset reduced to top 5000 songs based on popularity/availability.

2. Similarity Calculation:
Lyrics similarity is calculated using cosine similarity.

Stored as a .pkl file to avoid recomputation.

3. Flask App (app.py):
Input: Song name.

Output: List of similar songs (top 5).

Uses preloaded df.pkl and similarity.pkl.

4. Model Training Notebook:
All preprocessing and similarity computation logic is in Model Training.ipynb.

Allows reproducibility and further improvements.
