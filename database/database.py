from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./dboptical.db" 
#DATABASE_URL = "sqlite:///../dboptical.db" 

connect_arg={"timeout": 30,"check_same_thread": False}
engine = create_engine(DATABASE_URL,connect_args=connect_arg,pool_size=10, max_overflow=20)
SessionLocal = sessionmaker(bind=engine,autoflush=False)
Base = declarative_base()