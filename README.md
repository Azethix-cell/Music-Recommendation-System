# Music-Recommendation-System
🔊 Project Description: Music Recommendation System This project is a content-based music recommendation system built using natural language processing and machine learning. It analyzes the lyrics of songs to recommend similar music tracks.  

📌 How It Works:
It uses the lyrics of songs to compute textual similarity.

Upon entering a song name, it finds similar songs based on cosine similarity between vectorized lyrics.

The system is served through a web interface using Flask.

🧰 Technical Stack
Layer	Technology
Frontend	HTML (basic, handled via Flask templates)
Backend	Python, Flask
Data Processing	Pandas, NumPy
NLP / ML	scikit-learn (TF-IDF Vectorizer, Cosine Similarity)
Model Serialization	pickle for saving precomputed data
Dataset	spotify_millsongdata.csv – Songs and lyrics dataset
Deployment	Localhost Flask App (app.py)

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
