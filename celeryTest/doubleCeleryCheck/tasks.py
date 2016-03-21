from celery import *

#TCP/IP socket programming libraries for Modbus
import sys
#add logging capability
import logging
import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp

app = Celery('tasks', backend='amqp',
                      broker='amqp://Prafulla:praf1249@localhost/py_env')
i2_app = Celery('tasks_i2', backend='amqp',
                      broker='amqp://')

@app.task(name='ASUi3dea.tasks.add')
def add(x):
    if x==1:
        return "Successfully Turned on!! "
    if x==0:
        return "Successfully Turned off!! "
    #f3 = open("/sys/class/simul/simul_char/turnswitch","r")
    #return f3.read(10)

@i2_app.task(name='i2.pull_data')
def pull_values(id):
     master = modbus_tcp.TcpMaster()                                      
     master.set_timeout(5.0)                                              
     value = master.execute(1, cst.READ_HOLDING_REGISTERS, 100, 1)        
     dict={}
     dict['temperature'] = str(value[0])
     value = master.execute(1, cst.READ_HOLDING_REGISTERS, 100, 1)
     dict['voltage'] = str(value[0])
     value = master.execute(1, cst.READ_HOLDING_REGISTERS, 100, 1)        
     dict['current'] = str(value[0])
     value = master.execute(1, cst.READ_HOLDING_REGISTERS, 100, 1)        
     dict['quality'] = 'Good'
