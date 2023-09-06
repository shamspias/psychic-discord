from sqlalchemy import create_engine
from config.development import CONFIG

DATABASE_URL = CONFIG["DATABASE_URL"]
engine = create_engine(DATABASE_URL, echo=True)
