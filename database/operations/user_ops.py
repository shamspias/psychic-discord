from sqlalchemy.orm import sessionmaker
from database.models.user import User
from database import engine

Session = sessionmaker(bind=engine)


def add_user(discord_id, username):
    """Add a user to the database."""
    session = Session()
    user = User(discord_id=discord_id, username=username)
    session.add(user)
    session.commit()
    session.close()


def get_user(discord_id):
    """Retrieve a user from the database by their Discord ID."""
    session = Session()
    user = session.query(User).filter_by(discord_id=discord_id).first()
    session.close()
    return user


def update_username(discord_id, new_username):
    """Update the username of a user in the database."""
    session = Session()
    user = session.query(User).filter_by(discord_id=discord_id).first()
    if user:
        user.username = new_username
        session.commit()
    session.close()
