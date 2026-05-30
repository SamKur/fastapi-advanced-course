import json
from locust import HttpUser, task, between # locust for load testing (generally in testing, for prod we need monitoring tools like grafana)

"Run this file using cmd - locust"

class APIUser(HttpUser): # simulates a real world user
    wait_time = between(1, 2.5)

    @task
    def call_predict(self):
        payload = {
            'feature1': 1.0,
            'feature2': 2.0
        }
        headers = {'Content-Type': 'application/json'}
        self.client.post('/predict', data=json.dumps(payload), headers=headers)
                    # self.client -> Inheritance from HttpUser constructor

    @task(1)    # weight defaults to 1; probability = this wt/total wt . more wt == more load test
    def call_root(self):
        self.client.get('/')