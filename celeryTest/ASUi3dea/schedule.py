
from __future__ import absolute_import
from tasks import *

add = add.delay(4,5)
if(add.result() == false):
   print "data sent"


