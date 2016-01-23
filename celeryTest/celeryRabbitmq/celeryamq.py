import time
from celery import Celery

app = Celery('celeryrabbitmq', backend='amqp', broker='amqp://')

@app.task(ignore_result=True)
def print_hello():
    print 'hello there'

@app.task
def gen_data(x):
     print "Sending data"
     
     time.sleep(40)
     print "data sent"
     
     return 100        
