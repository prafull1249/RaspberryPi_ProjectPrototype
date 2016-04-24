import simplejson as json                                              
import requests                                                        
from celery import *                                  
                                                      
celery_i2 = Celery('tasks', backend='amqp',                 
                      broker='amqp://Prafulla:praf1249@localhost/py_env')       
from tasks import pull_values
                                                                      
#TCP/IP socket programming libraries for Modbus                        
import sys                                                             
#add logging capability                                                
import logging                                                         
import modbus_tk                                                       
import modbus_tk.defines as cst                                        
import modbus_tk.modbus_tcp as modbus_tcp                              
import requests                                                               
import time
                                                                       
@celery_i2.task                                                           
def add(x, y):                                                         
    return x + y                                                       
                                                                       
                                                                       
@celery_i2.task                                                           
def mul(x, y):                                                         
    #mul.delay(1,3)                                                    
    return x * y                                                       
                                                                       
@celery_i2.task                                                           
def xsum(numbers):                                                     
    return sum(numbers)                                                
                                                                       
"""
@celery_i2.task(name='remote.pull_data')                                
def pull_data(inverter_id):                                                  
     dict = {}
     dict = pull_values.delay(inverter_id)
     jsonStr =  json.dumps(dict.get())                                             
     print(jsonStr)                                                          
     return jsonStr                                                          
@celery_i2.task(name='i2.pull_data')
def pull_values(id):
    master = tcp.TcpMaster("127.0.0.1")
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
        dict['status'] = "sleeping"
    elif val_status[0] == 1:
        dict['status'] = "off"
    else:
        dict['status'] = "on"
    
    dict['temperature'] = str(val_temp[0])
    dict['ACPower'] = str(val_ac_power[0])
    dict['DCPower'] = str(val_dc_power[0])
    dict['lat'] = "33.3059398"
    dict['lon'] = "-111.6792469"
    dict['inverter'] = "1"
    return dict
""" 
@celery_i2.task(name='i2.pull_data')
def pull_data(): 
    for i in range(0,12):
        result = pull_values()
        result_v = result()
        response = requests.post("http://129.219.216.202:8000/ASUi3dea/update/",params=result_v)
        time.sleep(10) 
