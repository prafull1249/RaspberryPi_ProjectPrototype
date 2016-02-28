from celery import *

app = Celery('tasks', backend='amqp',
                      broker='amqp://Prafulla:praf1249@localhost/py_env')
@app.task(name='ASUi3dea.tasks.add')
def add(x):
    if x==1:
        return "Successfully Turned on!! "
    if x==0: 
        return "Successfully Turned off!! "
    #f3 = open("/sys/class/simul/simul_char/turnswitch","r")
    #return f3.read(10)
