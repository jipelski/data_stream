from sqlalchemy.orm import Session
from models import SensorData
from datetime import datetime


def create_entry(db: Session, sensor_id: str, location: str, value: float, time_stamp: datetime):
    db_data = SensorData(sensor_id=sensor_id, location=location, value=value, time_stamp=time_stamp)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data


def get_data(db: Session, sensor_id: str = None, location: str = None, start_time: datetime = None,
             end_time: datetime = None):
    query = db.query(SensorData)
    if sensor_id:
        query = query.filter(SensorData.sensor_id == sensor_id)
    if location:
        query = query.filter(SensorData.location == location)
    if start_time:
        query = query.filter(SensorData.time_stamp >= start_time)
    if end_time:
        query = query.filter(SensorData.time_stamp <= end_time)
    return query.all()
