from sqlalchemy import Column, Integer, String, Sequence
from .base import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    discord_id = Column(String(255), unique=True, nullable=False)
    username = Column(String(255), nullable=False)
