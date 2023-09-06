from sqlalchemy.orm import sessionmaker
from database.models.playlist import Playlist
from database import engine

Session = sessionmaker(bind=engine)


def add_song(user_id, song_name, song_url):
    """Add a song to a user's playlist in the database."""
    session = Session()
    new_song = Playlist(user_id=user_id, song_name=song_name, song_url=song_url)
    session.add(new_song)
    session.commit()
    session.close()


def remove_song(user_id, song_name):
    """Remove a song from a user's playlist in the database."""
    session = Session()
    song = session.query(Playlist).filter_by(user_id=user_id, song_name=song_name).first()
    if song:
        session.delete(song)
        session.commit()
    session.close()


def get_playlist(user_id):
    """Retrieve a user's playlist from the database."""
    session = Session()
    songs = session.query(Playlist).filter_by(user_id=user_id).all()
    session.close()
    return [(song.song_name, song.song_url) for song in songs]
