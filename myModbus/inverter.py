from modbus import *
from modbus_tcp import *
from execptions import *
from defines import *
from utils import *
from registers import *

class inverter(Slave):
    """
    The class is used to create inverter objects which will act as slaves in the tcp ip modbus communication with the raspberry pi. They will emulate the inverter class.
    """
    def __init__(self):
	"""
	constructor
	"""
	self.dict_holding = {}
	for i in range(4001):

