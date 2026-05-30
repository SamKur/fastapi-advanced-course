import time
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()

""" The function-based middleware: Small, one-off tasks
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    # 1. Pre-processing (before reaching the route)
    response = await call_next(request)
    # 2. Post-processing (after route finishes)
    response.headers["X-Process-Time"] = "0.01s"
    return response
"""

# The class-based middleware: More complex, reusable logic
class TimerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # STEP 1: Pre-processing (Starts here)
        start_time = time.time()

        # STEP 2: The Hand-off
        # The middleware "pauses" here. Control moves to the route below.
        response = await call_next(request)

        # STEP 4: Post-processing (Back in the middleware)
        # This only runs AFTER the 'hello' function is completely finished.
        duration = time.time() - start_time
        print(f'Request: {request.url.path} processed in {duration:.5f} seconds')
        return response


app.add_middleware(TimerMiddleware)

@app.get('/hello')
async def hello():
    # STEP 3: Route handler logic
    for _ in range(10000):
        pass
        print(_)
    return {'message': 'Hello World!'} # Now we head back up to STEP 4. this dict -> a fastapi.Response object