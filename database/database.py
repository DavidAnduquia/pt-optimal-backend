from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#DATABASE_URL = "sqlite:///./dboptical.db" 
#DATABASE_URL = "sqlite:///../dboptical.db" 
DATABASE_URL = "postgresql://pt_optimal_db_f7cz_user:S2h2TCo8zXQPUDfXRCf4sTuWx8AEe5x1@dpg-csbh6ejtq21c73a0dmfg-a.oregon-postgres.render.com:5432/pt_optimal_db_f7cz"
#connect_arg={"timeout": 30,"check_same_thread": False}

# Crea la conexión sin el parámetro timeout
engine = create_engine(DATABASE_URL,pool_size=10, max_overflow=20)
SessionLocal = sessionmaker(bind=engine,autoflush=False)
Base = declarative_base()