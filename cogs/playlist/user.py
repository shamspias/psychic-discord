class UserPlaylist:
    def __init__(self, user_id):
        self.user_id = user_id
        self.playlist_manager = PlaylistManager(user_id)

    def add_song(self, song_name, song_url):
        """Add a song to the playlist."""
        self.playlist_manager.add_song_to_playlist(song_name, song_url)

    def remove_song(self, song_name):
        """Remove a song from the playlist."""
        self.playlist_manager.remove_song_from_playlist(song_name)

    def view_playlist(self):
        """View the current playlist."""
        return self.playlist_manager.get_user_playlist()
