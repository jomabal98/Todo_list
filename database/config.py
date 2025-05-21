from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+pg8000://todo_user:1234@localhost:5432/todo_list"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)