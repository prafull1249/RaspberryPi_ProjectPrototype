class Master(object):
    """
    This class implements the Modbus Application protocol for a master
    To be subclassed with a class implementing the MAC layer
    """

    def __init__(self, timeout_in_sec, hooks=None):
        """Constructor: can define a timeout"""
        self._timeout = timeout_in_sec
        self._verbose = False
        self._is_opened = False

    def __del__(self):
        """Destructor: close the connection"""
        self.close()

    def set_verbose(self, verbose):
        """print some more log prints for debug purpose"""
        self._verbose = verbose

    def open(self):
        """open the communication with the slave"""
        if not self._is_opened:
            self._do_open()
            self._is_opened = True

    def close(self):
        """close the communication with the slave"""
        if self._is_opened:
            self._do_close()
            self._is_opened = False

    def _do_open(self):
        """Open the MAC layer"""
        raise NotImplementedError()

    def _do_close(self):
        """Close the MAC layer"""
        raise NotImplementedError()

    def _send(self, buf):
        """Send data to a slave on the MAC layer"""
        raise NotImplementedError()

    def _recv(self, expected_length):
        """
        Receive data from a slave on the MAC layer
        if expected_length is >=0 then consider that the response is done when this
        number of bytes is received
        """
        raise NotImplementedError()

    def _make_query(self):
        """
        Returns an instance of a Query subclass implementing
        the MAC layer protocol
        """
        raise NotImplementedError()

    @threadsafe_function
    def execute_func(self, slave, function_code, starting_address, quantity_of_x=0, ouput_value=0, data_format="", expected_length=-1):
	"""
	The execute_func takes a function_code and executes it on the slave address returning the required data_format according tothe fucntion_code
        """
	pdu = ""
    	is_read_function = False
	num_digits = 0
 	
	self.open()
	

	 if function_code == defines.READ_COILS or function_code == defines.READ_DISCRETE_INPUTS:
            is_read_function = True
            pdu = struct.pack(">BHH", function_code, starting_address, quantity_of_x)
            byte_count = quantity_of_x // 8
            if (quantity_of_x % 8) > 0:
                byte_count += 1
            nb_of_digits = quantity_of_x
            if not data_format:
                data_format = ">" + (byte_count * "B")
            if expected_length < 0:
                # No length was specified and calculated length can be used:
                # slave + func + bytcodeLen + bytecode + crc1 + crc2
                expected_length = byte_count + 5

	if function_code == defines.READ_INPUT_REGISTERS or function_code == READ_HOLDING_REGISTERS :
	   is_read_function = True
	   pdu = struct.pack(">BHH",function_code, starting_address, quantity_of_x)
           if not data_format:
                data_format = ">" + (quantity_of_x * "H")
           if expected_length < 0:
                # No length was specified and calculated length can be used:
                # slave + func + bytcodeLen + bytecode x 2 + crc1 + crc2
                expected_length = 2 * quantity_of_x + 5

    	elif (function_code == defines.WRITE_SINGLE_COIL) or (function_code == defines.WRITE_SINGLE_REGISTER):
            if function_code == defines.WRITE_SINGLE_COIL:
                if output_value != 0:
                    output_value = 0xff00
            fmt = ">BH"+("H" if output_value >= 0 else "h")
            pdu = struct.pack(fmt, function_code, starting_address, output_value)
            if not data_format:
                data_format = ">HH"
            if expected_length < 0:
                # No length was specified and calculated length can be used:
                # slave + func + adress1 + adress2 + value1+value2 + crc1 + crc2
                expected_length = 8

        elif function_code == defines.WRITE_MULTIPLE_COILS:
            byte_count = len(output_value) // 8
            if (len(output_value) % 8) > 0:
                byte_count += 1
            pdu = struct.pack(">BHHB", function_code, starting_address, len(output_value), byte_count)
            i, byte_value = 0, 0
            for j in output_value:
                if j > 0:
                    byte_value += pow(2, i)
                if i == 7:
                    pdu += struct.pack(">B", byte_value)
                    i, byte_value = 0, 0
                else:
                    i += 1
            if i > 0:
                pdu += struct.pack(">B", byte_value)
            if not data_format:
                data_format = ">HH"
            if expected_length < 0:
                # No length was specified and calculated length can be used:
                # slave + func + adress1 + adress2 + outputQuant1 + outputQuant2 + crc1 + crc2
                expected_length = 8

        elif function_code == defines.WRITE_MULTIPLE_REGISTERS:
            byte_count = 2 * len(output_value)
            pdu = struct.pack(">BHHB", function_code, starting_address, len(output_value), byte_count)
            for j in output_value:
                fmt = "H" if j >= 0 else "h"
                pdu += struct.pack(">" + fmt, j)
            if not data_format:
                data_format = ">HH"
            if expected_length < 0:
                # No length was specified and calculated length can be used:
                # slave + func + adress1 + adress2 + outputQuant1 + outputQuant2 + crc1 + crc2
                expected_length = 8

        elif function_code == defines.READ_EXCEPTION_STATUS:
            pdu = struct.pack(">B", function_code)
            data_format = ">B"
            if expected_length < 0:
                # No length was specified and calculated length can be used:
                expected_length = 5

        elif function_code == defines.DIAGNOSTIC:
            # SubFuncCode  are in starting_address
            pdu = struct.pack(">BH", function_code, starting_address)
            if len(output_value) > 0:
                for j in output_value:
                    # copy data in pdu
                    pdu += struct.pack(">B", j)
                if not data_format:
                    data_format = ">" + (len(output_value) * "B")
                if expected_length < 0:
                    # No length was specified and calculated length can be used:
                    # slave + func + SubFunc1 + SubFunc2 + Data + crc1 + crc2
                    expected_length = len(output_value) + 6

        elif function_code == defines.READ_WRITE_MULTIPLE_REGISTERS:
            is_read_function = True
            byte_count = 2 * len(output_value)
            pdu = struct.pack(
                ">BHHHHB",
                function_code, starting_address, quantity_of_x, defines.READ_WRITE_MULTIPLE_REGISTERS,
                len(output_value), byte_count
            )
            for j in output_value:
                fmt = "H" if j >= 0 else "h"
                # copy data in pdu
                pdu += struct.pack(">"+fmt, j)
            if not data_format:
                data_format = ">" + (quantity_of_x * "H")
            if expected_length < 0:
                # No lenght was specified and calculated length can be used:
                # slave + func + bytcodeLen + bytecode x 2 + crc1 + crc2
                expected_length = 2 * quantity_of_x + 5
        else:
            raise ModbusFunctionNotSupportedError("The {0} function code is not supported. ".format(function_code))

	
