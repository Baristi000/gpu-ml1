from time import sleep
from config import var

def gpu():
    while var.check1:
        sleep(0.1)
        var.time1 += 0.1

def non_gpu():
    while var.check2:
        sleep(0.1)
        var.time2 += 0.1
