# https://docs.locust.io/en/latest/writing-a-locustfile.html
# https://docs.locust.io/en/latest/installation.html

from locust import HttpLocust, TaskSet, task, between

class BoustonPredictionTasks(TaskSet):

    @task(1)
    def hello_world(self):
        self.client.get("/")

    @task(10)
    def predict(self):
        self.client.post("/predict", json={  
            "CHAS":{  
                "0":0
            },
            "RM":{  
                "0":6.575
            },
            "TAX":{  
                "0":296.0
            },
            "PTRATIO":{  
                "0":15.3
            },
            "B":{  
                "0":396.9
            },
            "LSTAT":{  
                "0":4.98
            },
            "LAWN": {
                    "0": 29
                },
                "FEE": {
                    "0": 300
                },
                "CAPE": {
                    "0": 29
                },
                "TIO": {
                    "0": 75.3
                },
                "J": {
                    "0": 299
                },
                "PT": {
                    "0": 88
                },
                "TEST": {
                    "0": 89
                }
        })
class LocustRunner(HttpLocust): 
    wait_time = between(0.5, 3.0)
    task_set = BoustonPredictionTasks
