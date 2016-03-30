import modbus
import modbus_tcp as tcp
import defines as cst
master = tcp.TcpMaster("192.168.1.110")
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

Hello Brenda,
Apologies for the delay. Coming back to your query, this is a tricky question(its categorized as a difficult level question) and the key was to choose the best fit answer. I tried to come up with a convincing explanation to eliminate each option as per the semantics of each option.

Pthread refers to _______
the POSIX standard.
POSIX standard is an IEEE standard. The option is partially correct  as Pthreads refers to more than what a POSIX standard is.
an implementation for thread behavior.
The textbook quote(section 4.4.1 pg 172) mentions that Pthreads is " a specification for thread behavior not an implementation". So this cannot be the correct answer.
a specification for thread behavior.
The semantics of this option seem correct and go with textbook quote(section 4.4.1 pg 172) that  Pthread is a specification for thread behavior. 
an API for process creation and synchronization
The API for process creation and synchronization does not completely explain what Pthreads refers to as it should be a POSIX standard defining an API for thread creation and synchronization.
I understand that this question is a bit difficult to answer given its close options. Anyways, I hope the above explanation helps you understand it better.






