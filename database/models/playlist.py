from sqlalchemy import Column, Integer, String, ForeignKey, Sequence
from sqlalchemy.orm import relationship
from .base import Base


class Playlist(Base):
    __tablename__ = 'playlists'
    id = Column(Integer, Sequence('playlist_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User")
    song_name = Column(String(255))
    song_url = Column(String(512))
