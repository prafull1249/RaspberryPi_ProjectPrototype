import simplejson as json                                              
import requests                                                        
from celery import *                                  
                                                      
celery_i2 = Celery('tasks', backend='amqp',                 
                      broker='amqp://Prafulla:praf1249@localhost/py_env')                                   
                                                                      
#TCP/IP socket programming libraries for Modbus                        
import sys                                                             
#add logging capability                                                
import logging                                                         
import modbus_tk                                                       
import modbus_tk.defines as cst                                        
import modbus_tk.modbus_tcp as modbus_tcp                              
                                                                       
                                                                       
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
                                                                       
@celery_i2.task(name='remote.pull_data')                                
def pull_data(inverter_id):                                                  
     dict = {}
     dict = pull_values.delay(inverter_id)
     jsonStr =  json.dumps(dict.get())                                             
     print(jsonStr)                                                          
     return jsonStr                                                          

@celery_i2.task(name='i2.pull_data')
def pull_values(id):
    return "something is executing"
    
