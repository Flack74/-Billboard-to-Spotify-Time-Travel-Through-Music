---
# 🎶 Billboard to Spotify: Time Travel Through Music

Ever wished you could relive the musical vibes of a past era? Now you can! This project lets you create a Spotify playlist filled with the Billboard Hot 100 hits from any date in history. Just input the date you’re curious about, and watch as your Spotify playlist transforms into a musical time capsule.

## ✨ Features

- **Historical Hit Parade**: Dive into the Billboard Hot 100 from any given date.
- **Spotify Playlist Wizardry**: Automatically creates a playlist on Spotify with the top hits from that date.
- **Flexible Date Input**: Explore any date in the `YYYY-MM-DD` format.

## 🚀 Getting Started

### 1. Clone the Repository

First, get your hands on the code:

```bash
git clone https://github.com/yourusername/billboard-to-spotify.git
cd billboard-to-spotify
```

### 2. Install Dependencies

You’ll need a few Python libraries to get this show on the road:

```bash
pip install requests beautifulsoup4 spotipy
```

### 3. Set Up Spotify API

- **Get Spotify Credentials**: Head over to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) and create a new app to grab your `CLIENT_ID` and `CLIENT_SECRET`.
- **Configure Redirect URI**: Set it to `http://localhost:8888/callback` in your Spotify app settings.

### 4. Configure Environment Variables

Set up your environment variables in a `.env` file or directly in your system:

```plaintext
CLIENT_ID=your_spotify_client_id
CLIENT_SECRET=your_spotify_client_secret
```

## 🎸 How to Use

1. **Run the Script**

   Execute the script to start your musical journey:

   ```bash
   python main.py
   ```

2. **Enter the Date**

   When prompted, type in the date in the format `YYYY-MM-DD`. 

   Example:
   ```plaintext
   Which year you want to travel to? Type date in this format YYYY-MM-DD: 1985-05-25
   ```

3. **Enjoy Your Playlist**

   - The script will create a private playlist on your Spotify account with the top hits from the specified date.
   - You’ll see URIs of found tracks and a message if any track wasn’t available on Spotify.

## 🔍 What’s Happening Under the Hood?

- **Date Magic**: Parses and validates the date you provide.
- **Web Scraping Sorcery**: Uses BeautifulSoup to pull song names from the Billboard Hot 100.
- **Spotify API Alchemy**: Searches for tracks on Spotify, creates a playlist, and fills it with hits.

## 🚧 Troubleshooting Tips

- **Wrong Date Format?**: Make sure you’re using `YYYY-MM-DD`.
- **HTTP Request Failed?**: Check your connection and make sure the URL is correct.
- **Spotify Authentication Problems?**: Double-check your credentials and redirect URI settings.

## 🌟 Contribute & Share

Got ideas for new features or improvements? Fork the repo, make your changes, and send a pull request. All contributions and suggestions are welcome!

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---
