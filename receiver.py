import os

FIFO = '/tmp/sopareplugin.fifo'
while True:
    with open(FIFO) as fifo:
        for line in fifo:
            print(line)
            open(FIFO,"r").close()