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
    def __init__(self, starting_address, size, name=''):
        """
        Contructor: defines the address range and creates the array of values
        """
        self.starting_address = starting_address
        self._data = [0] * size
        self.size = len(self._data)

    def is_in(self, starting_address, size):
        """
        Returns true if a block with the given address and size
        would overlap this block
        """
        if starting_address > self.starting_address:
            return (self.starting_address + self.size) > starting_address
        elif starting_address < self.starting_address:
            return (starting_address + size) > self.starting_address
        return True

    def __getitem__(self, item):
        """"""
        return self._data.__getitem__(item)

    def __setitem__(self, item, value):
        """"""
        call_hooks("modbus.ModbusBlock.setitem", (self, item, value))
        return self._data.__setitem__(item, value)

