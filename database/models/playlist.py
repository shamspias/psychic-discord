from sqlalchemy import Column, Integer, String, ForeignKey, Sequence
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .user import User

Base = declarative_base()


class Playlist(Base):
    __tablename__ = 'playlists'
    id = Column(Integer, Sequence('playlist_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User")  # This establishes the relationship with the User model
    song_name = Column(String(255))
    song_url = Column(String(512))
