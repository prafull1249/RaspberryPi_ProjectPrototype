from celery import *

app = Celery('tasks', backend='amqp',
                      broker='amqp://Prafulla:praf1249@localhost/py_env')
@app.task
def add2(x, y):
     #return x + y
    f3 = open("/sys/class/simul/simul_char/turnswitch","r")
    return f3.read(10)

@app.task(name='ASUi3dea.tasks.add')
def add(x):
    return "Successful"

@app.task(name='remote.pull_data')                                                     
def pull_data(inverter_id):                                      
     dict = {}                                                   
     dict = pull_values.delay(inverter_id)                       
     jsonStr =  json.dumps(dict)                                 
     print(jsonStr)                                              
     return jsonStr                                              
                                                                 

