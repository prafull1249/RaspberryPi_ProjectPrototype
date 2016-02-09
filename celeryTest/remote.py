from celery import *

app = Celery('tasks', backend='amqp',
                      broker='amqp://Prafulla:praf1249@localhost/py_env')
@app.task
def add(x, y):
     return x + y
