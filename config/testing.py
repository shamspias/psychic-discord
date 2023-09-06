import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

CONFIG = {
    "BOT_TOKEN": os.getenv("BOT_TOKEN"),
    "DATABASE_URL": os.getenv("DATABASE_URL"),
    "YOUTUBE_API_KEY": os.getenv("YOUTUBE_API_KEY"),
    "SPOTIFY_CLIENT_ID": os.getenv("SPOTIFY_CLIENT_ID"),
    "SPOTIFY_CLIENT_SECRET": os.getenv("SPOTIFY_CLIENT_SECRET"),
    "DISCORD_CLIENT_ID": os.getenv("DISCORD_CLIENT_ID"),
    "COMMAND_PREFIX": os.getenv("COMMAND_PREFIX")

}
