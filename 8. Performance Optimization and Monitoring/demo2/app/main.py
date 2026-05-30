from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

Instrumentator().instrument(app).expose(app)

# in grafana ui ie 3000 port add data source as docker_service_or_img_name:9090 like prometheus:9090
# not localhost:9090 because Docker handles networking and isolation. localhost would point to grafana's port

@app.get('/')
def root():
    return {'message': 'FastAPI with Prometheus, Grafana & Docker!'}


@app.get('/ping')
def ping():
    return {'message': 'pong'}