import asyncio
import websockets
import json
import random
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()


async def send_sensor_data():
    uri = os.getenv("WEBSOCKET_URI", "ws://localhost:8000/ws/add_data")

    async with websockets.connect(uri) as websocket:
        while True:
            sensor_data = {
                "sensor_id": f"sensor_{random.randint(1, 10)}",
                "location": random.choice(["Living Room", "Bedroom", "Kitchen", "Bathroom"]),
                "value": round(random.uniform(10.0, 30.0), 2),
                "time_stamp": datetime.utcnow().isoformat()
            }

            await websocket.send(json.dumps(sensor_data))

            print(f"Sent data: {sensor_data}")

            await asyncio.sleep(50)  # Adjust time between requests as needed


if __name__ == "__main__":
    asyncio.run(send_sensor_data())
