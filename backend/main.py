from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from models import SessionLocal, Base, engine, SensorData
import crud
from datetime import datetime
from pydantic import BaseModel
import os

app = FastAPI()

Base.metadata.create_all(bind=engine)

origins = os.getenv("ORIGINS", "").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class DataRequest(BaseModel):
    sensor_id: str
    location: str
    value: float
    time_stamp: datetime


@app.websocket("/ws/add_data")
async def websocket_add_data(websocket: WebSocket):
    await websocket.accept()
    db = SessionLocal()
    try:
        while True:
            data = await websocket.receive_json()
            if isinstance(data, dict):
                sensor_data = SensorData(**data)
                crud.create_entry(
                    db,
                    sensor_id=sensor_data.sensor_id,
                    location=sensor_data.location,
                    value=sensor_data.value,
                    time_stamp=sensor_data.time_stamp
                )
            elif isinstance(data, list):
                for item in data:
                    sensor_data = SensorData(**item)
                    crud.create_entry(
                        db,
                        sensor_id=sensor_data.sensor_id,
                        location=sensor_data.location,
                        value=sensor_data.value,
                        time_stamp=sensor_data.time_stamp
                    )
            await websocket.send_text("Data successfully stored.")
    except WebSocketDisconnect:
        pass
    finally:
        db.close()


@app.get("/get_all")
async def get_all(
        sensor_id: str = None,
        location: str = None,
        start_time: str = None,
        end_time: str = None,
        db: Session = Depends(get_db)
):
    start_time_dt = datetime.fromisoformat(start_time) if start_time else None
    end_time_dt = datetime.fromisoformat(end_time) if end_time else None
    data = crud.get_data(
        db,
        sensor_id=sensor_id,
        location=location,
        start_time=start_time_dt,
        end_time=end_time_dt
    )
    return data
