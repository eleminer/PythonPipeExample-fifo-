import os
import time
path = "/tmp/sopareplugin.fifo"
try:
    os.remove(path)
except OSError:
    pass

os.mkfifo(path)
fifo = open(path, "w")
Data="nothing"
i=0

def sendingpipe():
    global Data, i
    fifo = open(path, "w")
    print("sending")
    i=i+1
    fifo.write("DataString!"+str(i)+str(Data)+"\r\n")
    fifo.close()

while True:
    sendingpipe()
    #time.sleep(0.5)