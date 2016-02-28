import time 
from proj.tasks import *
from proj.celery import celery
import requests

@celery.task
def requests_func():
   #for i in range(0,3):
   #str = get_data.delay()
   #str = get_cpufreq.delay()
   str = getndump_inverter_data.delay()
   while(str.ready() == False):
       time.sleep(3)
   print str.get()

   #requests_func()
