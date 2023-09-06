from database import engine  # importing the engine
from database.models.base import Base

# Import the models so they're recognized by SQLAlchemy
from database.models.user import User
from database.models.playlist import Playlist

if __name__ == "__main__":
    # Create the tables
    Base.metadata.create_all(engine)
