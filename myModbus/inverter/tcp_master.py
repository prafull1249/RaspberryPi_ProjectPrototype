import modbus
import modbus_tcp as tcp
import defines as cst
master = tcp.TcpMaster("127.0.0.1")
master.set_timeout(5.0)

print "Voltage read two times as follows" 
print master.execute(1, cst.READ_HOLDING_REGISTERS, 40080,2)
print  master.execute(1, cst.READ_HOLDING_REGISTERS, 40080,2)

print "Current read two times as follows" 
print master.execute(1, cst.READ_HOLDING_REGISTERS, 40075,2)
print master.execute(1, cst.READ_HOLDING_REGISTERS, 40075,3)

print "Frequency read two times as follows" 
print master.execute(1, cst.READ_HOLDING_REGISTERS, 40086,2)
print master.execute(1, cst.READ_HOLDING_REGISTERS, 40086,2)

print "Power read two times as follows" 
print master.execute(1, cst.READ_HOLDING_REGISTERS, 40084,2)
print master.execute(1, cst.READ_HOLDING_REGISTERS, 40084,2)



