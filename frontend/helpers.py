from dotenv import load_dotenv
import os
import requests

load_dotenv()

api_key = os.getenv('TRACK_API_KEY')
base_url = "https://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key="
album_not_avail = "https://discussions.apple.com/content/attachment/592590040"

def get_album_pic(artist_name, song_name):
	response = requests.get(base_url + api_key + "&artist=" + artist_name + "&track=" + song_name + "&format=json")

	if response.status_code == 200:
		data = response.json()
		if "track" in data and "album" in data["track"] and "image" in data["track"]["album"]:
			for image in data["track"]["album"]["image"]:
				if image["size"] == "extralarge" and image["#text"] != "":
					return image["#text"]
		
	return album_not_avail

def get_track_link(artist_name, song_name):
	response = requests.get(base_url + api_key + "&artist=" + artist_name + "&track=" + song_name + "&format=json")

	if response.status_code == 200:
		data = response.json()
		if "track" in data and "url" in data["track"]:
			return data["track"]["url"]
	
	return ""