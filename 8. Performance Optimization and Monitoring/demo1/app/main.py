from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
import uvicorn

app = FastAPI()

Instrumentator().instrument(app).expose(app)


@app.get('/')
def root():
    return {'message': 'FastAPI with Prometheus and Docker!'}

# package this entire app using -> docker compose up --build

if __name__ == "__main__":  # just to run the script directly using cmd -> python main.py
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)   # "filename:object" format