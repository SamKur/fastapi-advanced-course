import time
from fastapi import FastAPI

app = FastAPI()


def computation(n: int):
    res = 0
    for i in range(n):
        res += (i * 2)
    time.sleep(1)
    return res


@profile    # isolated func to profile... later run via cmd -> kernprof -l -v profiling_test.py
def process_data(x: int):
    return computation(x)


@app.get('/profiling')
def profiling(a: int):
    return {'result': process_data(a)}