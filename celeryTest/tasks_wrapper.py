import time 
from proj.tasks import *

for i in range(0,4):
    result = add.delay(i,20)
    while(result.ready() == False):
        time.sleep(5) 
