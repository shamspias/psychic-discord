import requests


class YouTubeIntegration:
    BASE_URL = "https://www.googleapis.com/youtube/v3"

    def __init__(self, api_key):
        self.api_key = api_key

    def search_song(self, song_name):
        """Search for a song on YouTube and return the first result's URL."""
        search_url = f"{self.BASE_URL}/search?part=snippet&q={song_name}&key={self.api_key}"
        response = requests.get(search_url)
        results = response.json().get('items', [])

        if results:
            video_id = results[0]['id']['videoId']
            return f"https://www.youtube.com/watch?v={video_id}"

        return None
