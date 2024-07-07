# Sensor Data Streaming Project

This repository contains the full stack application for streaming sensor data using React (frontend), FastAPI (backend), and a gateway service to simulate data ingestion.

## Docker Images

The Docker images for this project are available on Docker Hub.

### Backend Service

The backend service is implemented using FastAPI.

#### Pulling the Docker Image

To pull the backend Docker image, run the following command:

```sh
docker pull jipelski/sensor_stream-backend:latest
```

#### Running the Docker Container

To run the backend Docker container, use the following command:

```sh
docker run -d --name backend -p 8000:8000 jipelski/sensor_stream-backend:latest
```

### Frontend Service

The frontend service is implemented using React.

#### Pulling the Docker Image

To pull the frontend Docker image, run the following command:

```sh
docker pull jipelski/sensor_stream-frontend:latest
```

#### Running the Docker Container

To run the frontend Docker container, use the following command:

```sh
docker run -d --name frontend -p 3000:3000 jipelski/sensor_stream-frontend:latest
```

### Gateway Service

The gateway service is used to simulate data ingestion.

#### Pulling the Docker Image

To pull the gateway Docker image, run the following command:

```sh
docker pull jipelski/sensor_stream-gateway:latest
```

#### Running the Docker Container

To run the gateway Docker container, use the following command:

```sh
docker run -d --name gateway jipelski/sensor_stream-gateway:latest
```

## Running the Full Stack Application with Docker Compose

To run the full stack application using Docker Compose, follow these steps:

1. Clone the repository:

    ```sh
    git clone https://github.com/jipelski/sensor_stream.git
    ```

2. Navigate to the project directory:

    ```sh
    cd sensor_stream
    ```
    
3. Run Docker Compose to start all services:

    ```sh
    docker-compose up -d
    ```

## Development Setup

To set up the development environment locally, follow these steps:

1. Clone the repository:

    ```sh
    git clone https://github.com/jipelski/sensor_stream.git
    ```

2. Navigate to the project directory:

    ```sh
    cd sensor_stream
    ```

3. Follow the instructions in each service's directory to set up the local environment.

### Backend Service

Navigate to the `backend` directory and set up the Python environment:

```sh
cd backend
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Frontend Service

Navigate to the `frontend` directory and set up the React environment:

```sh
cd frontend
npm install
npm start
```

### Gateway Service

Navigate to the `gateway` directory and set up the Python environment:

```sh
cd gateway
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python mock_gateway.py
```
