from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./krishi_connect.db")

if DATABASE_URL.startswith("postgresql://"):
    engine = create_engine(DATABASE_URL)
else:
        engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False })

# Database session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Base class for database models
Base = declarative_base()


# Database connection
def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
