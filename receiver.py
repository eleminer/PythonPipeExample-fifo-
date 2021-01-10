import os
import sys

path = "/tmp/sopareplugin.fifo"
fifo = open(path, "r")
while True:
    for line in fifo:
        print "Received: " + line,
fifo.close()