import joblib
import numpy as np
import pandas as pd
from typing import List

saved_model = joblib.load('model.joblib') # train and predict via same sklearn version
print('Loaded the Model')


def make_prediction(data: dict) -> float: # sending a row for prediction
    # features = np.array([
    #     [
    #         data['longitude'],
    #         data['latitude'],
    #         data['housing_median_age'],
    #         data['total_rooms'],
    #         data['total_bedrooms'],
    #         data['population'],
    #         data['households'],
    #         data['median_income']
    #     ]
    # ])
    # return saved_model.predict(features)[0] # as sending 1 row, will give 1 row inside the list
    df = pd.DataFrame([data])  # Convert dict to DataFrame with feature names
    return saved_model.predict(df)[0]  # Predict using DataFrame


def make_batch_predictions(data: List[dict]) -> np.array:
    # X = np.array([
    #     [
    #         x['longitude'],
    #         x['latitude'],
    #         x['housing_median_age'],
    #         x['total_rooms'],
    #         x['total_bedrooms'],
    #         x['population'],
    #         x['households'],
    #         x['median_income']
    #     ]
    #     for x in data
    # ])
    # return saved_model.predict(X)
    df = pd.DataFrame(data)  # Convert list of dicts to DataFrame with feature names
    return saved_model.predict(df)