
from __future__ import absolute_import

from proj.celery import celery


@celery.task
def add(x, y):
    return x + y


@celery.task
def mul(x, y):
    #mul.delay(1,3)
    return x * y


@celery.task
def xsum(numbers):
    return sum(numbers)

@celery.task
def get_data():
   fo = open("/dev/kmsg","r")
   str = fo.read(100)
   print "The open is successful :",str
   return str

@celery.task
def get_cpufreq():
    filep = open("/sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_min_freq","r")
    str = filep.read(20)
    print "The current frequency is ",str
    return str 

@celery.task
def get_inverter_data():
    fo = open("/sys/class/simul/simul_char/temp","r")
    f1 = open("/sys/class/simul/simul_char/health","r")
    f2 = open("/sys/class/simul/simul_char/uptime","r")
    f3 = open("/sys/class/simul/simul_char/turnswitch","r")
    f4 = open("/sys/class/simul/simul_char/prod","r")
    #fo = open("/dev/kmsg","r")
    
    str = fo.read(10)
    print "Temp :",str
    str = f1.read(10)
    print "health :",str
    str = f2.read(10)
    print "uptime :",str
    str = f3.read(10)
    print "turnswitch :",str
    str = f4.read(10)
    print "prod :",str
    fo.close()

