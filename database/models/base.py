from sqlalchemy.ext.declarative import declarative_base
from database import engine  # importing the engine

Base = declarative_base()

if __name__ == "__main__":
    from .user import User  # Import models to ensure they're created.
    from .playlist import Playlist

    Base.metadata.create_all(engine)
