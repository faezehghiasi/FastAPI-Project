from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

Base = declarative_base()

Session_Local = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = Session_Local()
    try:
        yield db
    finally:
        db.close()