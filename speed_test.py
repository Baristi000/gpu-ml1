import gpu, nongpu, test
from threading import Thread
from time import sleep
from config import var

l = []

l.append(Thread(target=gpu.gpu))
l.append(Thread(target=nongpu.non_gpu))
l.append(Thread(target=test.gpu))
l.append(Thread(target=test.non_gpu))
for t in l:
    t.start()
for t in l:
    t.join()

print("\n\ngpu execution time: "+str(var.time1))
print("cpu execution time: "+str(var.time2)+"\n\n")