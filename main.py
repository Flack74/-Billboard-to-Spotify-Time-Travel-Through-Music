import requests
from bs4 import BeautifulSoup
from datetime import datetime
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

# Get today's date
today = datetime.today().strftime("%Y-%m-%d")

# User input for the date
date = input("Which year you want to travel to? Type date in this format YYYY-MM-DD: ")

# Validate date input
try:
    datetime.strptime(date, "%Y-%m-%d")
except ValueError:
    print("Invalid date format. Please use YYYY-MM-DD.")
    exit()

# Form the URL dynamically
url = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(url)

# Check for a successful request
if response.status_code != 200:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
    exit()

# Parse the HTML response
soup = BeautifulSoup(response.text, "html.parser")

# Select song elements
songs = soup.select("li ul li .c-title")
song_names = [song.text.strip() for song in songs]

# Set up Spotipy with OAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id= os.environ.get("CLIENT_ID"),
    client_secret= os.environ.get("CLIENT_SECRET"),
    redirect_uri="http://localhost:8888/callback",
    scope="playlist-modify-private"
))

# Get current user ID
user_id = sp.current_user()['id']

# Search for songs and collect URIs
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")

    # Extract relevant information
    if result['tracks']['items']:
        track = result['tracks']['items'][0]
        song_name = track['name']
        song_uri = track['uri']
        song_uris.append(song_uri)
        print(f"Found track: {song_name}, URI: {song_uri}")
    else:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Create a new private playlist
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(f"Created playlist: {playlist['name']}")

# Add songs to the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print(f"Added {len(song_uris)} songs to the playlist.")
