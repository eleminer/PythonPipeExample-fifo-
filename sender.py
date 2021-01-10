import os
try:
    os.remove("/tmp/sopareplugin.fifo")
except OSError:
    pass

path = "/tmp/my_program2.fifo"
os.mkfifo(path)

fifo = open(path, "w")
while True:
    fifo.write("Message from the sender!\n")
fifo.close()