from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///./test.db"  # This is just an example using SQLite; replace with your actual database URL

engine = create_engine(DATABASE_URL, echo=True)  # echo=True will log SQL queries; turn it off in production
