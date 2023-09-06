import random


class SongQueue:
    def __init__(self):
        self.queue = []

    def add(self, song_url):
        """Add a song to the queue."""
        self.queue.append(song_url)

    def skip(self):
        """Skip the current song. Removes the song from the start of the queue."""
        if self.queue:
            self.queue.pop(0)

    def get_next_song(self):
        """Get the next song from the queue. Does not remove the song from the queue."""
        return self.queue[0] if self.queue else None

    def clear(self):
        """Clear the entire song queue."""
        self.queue.clear()

    def shuffle(self):
        """Shuffle the song queue."""
        random.shuffle(self.queue)

    def get_queue(self):
        """Return the entire song queue."""
        return self.queue

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0
