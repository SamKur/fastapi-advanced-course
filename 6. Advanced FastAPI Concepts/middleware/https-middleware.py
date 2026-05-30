from fastapi import FastAPI
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
# from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware # same

app = FastAPI()

app.add_middleware(HTTPSRedirectMiddleware)