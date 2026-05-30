from typing import List

import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from model import model

app = FastAPI()


class IrisFlower(BaseModel): # same order of features as in training data
    SepalLengthCm: float
    SepalWidthCm: float
    PetalLengthCm: float
    PetalWidthCm: float


@app.post('/predict')
def predict(data: IrisFlower):
    features = np.array([ # 2d because sklearn models ALWAYS expect 2d input
        [
            data.SepalLengthCm,
            data.SepalWidthCm,
            data.PetalLengthCm,
            data.PetalWidthCm
        ]
    ])
    prediction = model.predict(features)
    return {'prediction': int(prediction[0])} # as api response needs to be scalar

@app.post('/batch_predict')
def predict_batch(data: List[IrisFlower]):
    # Convert List of Objects -> 2D List -> 2D Numpy Array
    # Shape becomes (N, 4) where N is the number of flowers sent
    X = np.array([[f.SepalLengthCm, f.SepalWidthCm, f.PetalLengthCm, f.PetalWidthCm] for f in data])
    # Predict everything in one mathematical operation
    y_gen = model.predict(X) 
    # Return a list of results
    return {"predictions": y_gen.tolist()}