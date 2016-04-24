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
'''

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
'''

@i2_app.task
def pull_values():
    master = modbus_tcp.TcpMaster("127.0.0.1")
    master.set_timeout(5.0)

    print "DC power read as follows" 
    val_dc_power = master.execute(1, cst.READ_HOLDING_REGISTERS, 40101,2)
    print val_dc_power[0]

    print "AC Power read as follows" 
    val_ac_power = master.execute(1, cst.READ_HOLDING_REGISTERS, 40084,2)
    print val_ac_power[0]
    
    print "Status is as follows"
    val_status = master.execute(1, cst.READ_HOLDING_REGISTERS, 40108,2)
    print val_status[0]
    
    print "heatsink temperature is as follows"
    val_temp = master.execute(1, cst.READ_HOLDING_REGISTERS, 40104,2)
    print val_temp[0]
    dict={}
    
    if val_status[0] == 2:
        dict['status'] = "2"
    elif val_status[0] == 1:
        dict['status'] = "1"
    else:
        dict['status'] = "4"
    
    dict['temperature'] = str(val_temp[0])
    dict['ACPower'] = str(val_ac_power[0])
    dict['lat'] = "33.3059398"
    dict['lon'] = "-111.6792469"
    dict['inverter'] = "1"
    dict['DCPower'] = str(val_dc_power[0])
    return dict










