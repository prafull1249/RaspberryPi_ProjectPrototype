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
    def execute(
        self, slave, function_code, starting_address, quantity_of_x=0, output_value=0, data_format="", expected_length=-1):
        """
        Execute a modbus query and returns the data part of the answer as a tuple
        The returned tuple depends on the query function code. see modbus protocol
        specification for details
        data_format makes possible to extract the data like defined in the
        struct python module documentation
        """

        pdu = ""
        is_read_function = False
        nb_of_digits = 0

        # open the connection if it is not already done
        self.open()

        # Build the modbus pdu and the format of the expected data.
        # It depends of function code. see modbus specifications for details.
        if function_code == READ_COILS or function_code == READ_DISCRETE_INPUTS:
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

        elif function_code == READ_INPUT_REGISTERS or function_code == READ_HOLDING_REGISTERS:
            is_read_function = True
            pdu = struct.pack(">BHH", function_code, starting_address, quantity_of_x)
            if not data_format:
                data_format = ">" + (quantity_of_x * "H")
            if expected_length < 0:
                # No length was specified and calculated length can be used:
                # slave + func + bytcodeLen + bytecode x 2 + crc1 + crc2
                expected_length = 2 * quantity_of_x + 5