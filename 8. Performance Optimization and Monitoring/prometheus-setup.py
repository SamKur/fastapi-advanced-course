from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

Instrumentator().instrument(app).expose(app) # hooks && expose new /metric endpoint

# docker run --name prometheus -d -p 127.0.0.1:9090:9090 prom/prometheus
# http://127.0.0.1:9090/ to view metrics

@app.get('/home')
def home():
    return {'message': 'Prometheus Demo'}