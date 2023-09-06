from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Sequence
from sqlalchemy.ext.declarative import declarative_base
from .user import User

Base = declarative_base()


class Playlist(Base):
    __tablename__ = 'playlists'
    id = Column(Integer, Sequence('playlist_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    song_name = Column(String(255))
    song_url = Column(String(512))
