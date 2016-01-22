import time
from tasks import *
from celery import Celery


for i in range(0,4):
   result = gen_prime.delay(i * 1000)
   while(result.ready() == False):
       time.sleep(5)

