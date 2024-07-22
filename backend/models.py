import os
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime


DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("No DATABASE_URL set for the application")

engine = create_engine(
    DATABASE_URL,
    pool_size=15,
    max_overflow=30,
    pool_timeout=30,
    pool_recycle=1800
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class SensorData(Base):
    __tablename__ = "sensor_data"
    id = Column(Integer, primary_key=True, index=True)
    sensor_id = Column(String, index=True)
    location = Column(String, index=True)
    value = Column(Float)
    time_stamp = Column(DateTime, default=datetime.utcnow())


Base.metadata.create_all(bind=engine)
