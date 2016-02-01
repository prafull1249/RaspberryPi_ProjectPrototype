import time 
from proj.tasks import *

for i in range(0,3):
   #str = get_data.delay()
   str = get_cpufreq.delay()
   while(str.ready() == False):
        time.sleep(3)
   print str.get()
   print " looop over ",i

