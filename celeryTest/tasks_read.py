
fo = open("/dev/kmsg","r")
str = fo.read(100)
print "The open is successful :",str
fo.close()
