from pydantic import BaseModel
from datetime import datetime


class SensorDataBase(BaseModel):
    sensor_id: str
    location: str
    value: float
    timestamp: datetime


class SensorDataCreate(SensorDataBase):
    pass


class SensorData(SensorDataBase):
    id: int

    class Config:
        orm_mode = True
