# Audio Analyzer Microservice

A lightweight FastAPI-based microservice that simulates audio file analysis and returns metadata.

## Features
- Upload audio files via `/analyze-audio/` endpoint
- Fake metadata generation (simulated audio analysis)
- REST API with FastAPI
- Dockerized for easy deployment

## Running Locally

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Run with Uvicorn:
    ```bash
    uvicorn app.main:app --reload
    ```

3. Or run in Docker:
    ```bash
    docker build -t audio-analyzer .
    docker run -p 8000:8000 audio-analyzer
    ```

4. Visit the API docs at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## API Endpoints

### GET /health
Returns the health status of the API.

Response:
```json
{
    "status": "ok"
}
