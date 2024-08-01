import pickle
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
from helpers import get_album_pic
from helpers import get_track_link

song_list = pickle.load(open("artifacts/song_list.pkl", "rb"))
song_data = pickle.load(open("artifacts/song_data.pkl", "rb"))

st.set_page_config(
   page_title="Song Recommendations",
)

st.header("Song Recommendations")

selected = st.selectbox("Please type or select a song", song_list)

def recommend_songs(song_name, song_artist):
    # Get index of song
    song_data_idx = song_data[(song_data['track_name'] == song_name) & (song_data["track_artist"] == song_artist)].index[0]
    
    # get textual info of song
    year = song_data.loc[song_data_idx, "year"]
    song_id = song_data.loc[song_data_idx, "track_id"]
    album = song_data.loc[song_data_idx, "track_album_name"]
    genre = song_data.loc[song_data_idx, "playlist_genre"]
    subgenre = song_data.loc[song_data_idx, "playlist_subgenre"]

    # smaller df for songs within its time period and genre
    smaller_df = song_data[(song_data["year"] <= year + 2) & 
                (song_data["year"] >= year - 2) & 
                  (song_data["playlist_subgenre"] == subgenre)].reset_index(drop=True)

    features = smaller_df[['danceability',
       'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness',
       'instrumentalness', 'liveness', 'valence', 'tempo']]

    # normalize numerical music data
    scaler = MinMaxScaler()
    normalized_data = pd.DataFrame(scaler.fit_transform(features), columns=features.columns)
    
    # create similarity matrix
    similarity_matrix = cosine_similarity(normalized_data)

    # Get similarity scores for the given item
    idx = smaller_df[(smaller_df['track_name'] == song_name) 
                    & (smaller_df["track_artist"] == song_artist)].index[0]    
    similarity_scores = similarity_matrix[idx]

    # Get indices of the most similar items
    similar_indices = np.argsort(-similarity_scores)[:6]  # 1 more bc includes the item itself

    return smaller_df.iloc[similar_indices]

if st.button("Show recommended"):
	parts = selected.split(" by ")
	recs = recommend_songs(parts[0], parts[1])

	# skip 0 bc song itself
	rec1 = recs.iloc[1]
	rec2 = recs.iloc[2]
	rec3 = recs.iloc[3]
	rec4 = recs.iloc[4]
	rec5 = recs.iloc[5]

	col1,col2,col3,col4,col5 = st.columns(5)

	with col1:
		track_name = rec1["track_name"]
		track_artist = rec1["track_artist"]
		image_url = get_album_pic(track_artist, track_name)
		st.image(image_url, use_column_width=True)
		song_url = get_track_link(track_artist, track_name)
		if song_url == "":
			st.markdown(f"{track_name} by {track_artist}")
		else:
			st.markdown(f"""<style>a.custom-link {{color: #FFFFFF; /* Change this to your desired color */}}</style><a class="custom-link" href={song_url}>{track_name} by {track_artist}</a>""",unsafe_allow_html=True)	

	with col2:
		track_name = rec2["track_name"]
		track_artist = rec2["track_artist"]
		image_url = get_album_pic(track_artist, track_name)
		st.image(image_url, use_column_width=True)
		song_url = get_track_link(track_artist, track_name)
		if song_url == "":
			st.markdown(f"{track_name} by {track_artist}")
		else:
			st.markdown(f"""<style>a.custom-link {{color: #FFFFFF; /* Change this to your desired color */}}</style><a class="custom-link" href={song_url}>{track_name} by {track_artist}</a>""",unsafe_allow_html=True)
	with col3:
		track_name = rec3["track_name"]
		track_artist = rec3["track_artist"]
		image_url = get_album_pic(track_artist, track_name)
		st.image(image_url, use_column_width=True)
		song_url = get_track_link(track_artist, track_name)
		if song_url == "":
			st.markdown(f"{track_name} by {track_artist}")
		else:
			st.markdown(f"""<style>a.custom-link {{color: #FFFFFF; /* Change this to your desired color */}}</style><a class="custom-link" href={song_url}>{track_name} by {track_artist}</a>""",unsafe_allow_html=True)

	with col4:
		track_name = rec4["track_name"]
		track_artist = rec4["track_artist"]
		image_url = get_album_pic(track_artist, track_name)
		st.image(image_url, use_column_width=True)
		song_url = get_track_link(track_artist, track_name)
		if song_url == "":
			st.markdown(f"{track_name} by {track_artist}")
		else:
			st.markdown(f"""<style>a.custom-link {{color: #FFFFFF; /* Change this to your desired color */}}</style><a class="custom-link" href={song_url}>{track_name} by {track_artist}</a>""",unsafe_allow_html=True)

	with col5:
		track_name = rec5["track_name"]
		track_artist = rec5["track_artist"]
		image_url = get_album_pic(track_artist, track_name)
		st.image(image_url, use_column_width=True)
		song_url = get_track_link(track_artist, track_name)
		if song_url == "":
			st.markdown(f"{track_name} by {track_artist}")
		else:
			st.markdown(f"""<style>a.custom-link {{color: #FFFFFF; /* Change this to your desired color */}}</style><a class="custom-link" href={song_url}>{track_name} by {track_artist}</a>""",unsafe_allow_html=True)
