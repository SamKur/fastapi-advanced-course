from fastapi import FastAPI
from starlette.middleware.gzip import GZipMiddleware
# from fastapi.middleware.gzip import GZipMiddleware # same

app = FastAPI()

app.add_middleware(
    GZipMiddleware, minimum_size=1000
)