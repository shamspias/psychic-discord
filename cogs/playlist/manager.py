from database.operations import playlist_ops


class PlaylistManager:
    def __init__(self, user_id):
        self.user_id = user_id

    def add_song_to_playlist(self, song_name, song_url):
        """Add a song to the user's playlist."""
        playlist_ops.add_song(self.user_id, song_name, song_url)

    def remove_song_from_playlist(self, song_name):
        """Remove a song from the user's playlist."""
        playlist_ops.remove_song(self.user_id, song_name)

    def get_user_playlist(self):
        """Retrieve the user's playlist."""
        return playlist_ops.get_playlist(self.user_id)
