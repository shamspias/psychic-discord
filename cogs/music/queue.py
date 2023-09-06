class SongQueue:
    def __init__(self):
        self.queue = []

    def add(self, song_url):
        """Add a song to the queue."""
        self.queue.append(song_url)

    def skip(self):
        """Skip the current song."""
        if self.queue:
            self.queue.pop(0)

    def get_queue(self):
        """Return the current queue."""
        return self.queue
