from sqlalchemy import create_engine

DATABASE_URL = "mysql+pymysql://username:password@localhost/dbname"  # Replace with your actual MySQL connection details

engine = create_engine(DATABASE_URL, echo=True)  # echo=True will log SQL queries; turn it off in production
