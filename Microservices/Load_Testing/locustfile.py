# https://docs.locust.io/en/latest/writing-a-locustfile.html
# https://docs.locust.io/en/latest/installation.html

from locust import HttpUser, task, between

# # necessary imports
# from locust import HttpLocust, TaskSet, task
# # your own custom task set
# class CustomTaskSet(TaskSet):
#     # your task
#     @task(1) # how many times to run per execution cycle
#     def index(self): # task function definition
#         self.client.get('/') # hit '/' with a get request
# # task runner
# class LocustRunner(HttpLocust): 
#     task_set = CustomTaskSet # add your set to the task runner
#     min_wait = 5000
#     max_wait = 15000

class BoustonPredictionTestUser(HttpUser):
    wait_time = between(0.5, 3.0)

    def on_start(self):
        self.client.post("/login", json={"username":"foo", "password":"bar"})
        print('Locust test is starting!')

    def on_stop(self):
        print('Locust test is stopping!')

    @task(1)
    def hello_world(self):
        self.client.get("http://ip:5000")

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