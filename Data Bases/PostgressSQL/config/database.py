from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.todo_model import Base  # ✅ Import Base

POSTGRES_URI = "postgresql://neondb_owner:npg_1xkSPtjpwF6L@ep-calm-moon-a50kgph8-pooler.us-east-2.aws.neon.tech/neondb?sslmode=require"

engine = create_engine(POSTGRES_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ✅ Create tables only if they don’t exist
Base.metadata.create_all(bind=engine)