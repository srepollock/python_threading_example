#!/usr/bin/env python3
import math
import random
import threading
import time
def dft(inreal, inimage, outreal, outimage):
    n = len(inreal)
    for i in range(0, n):
            sumreal = 0
            sumimage = 0
            for t in range(0, n):
                    angle = float(2 * math.pi * t * i / n);
                    sumreal += float(float(inreal[t]) * float(math.cos(angle)) + float(inimage[t]) * float(math.sin(angle)))
                    sumimage += float(float(-inreal[t]) * float(math.sin(angle)) + float(inimage[t]) * float(math.cos(angle)))
            outreal[i] = float(sumreal)
            outimage[i] = float(sumimage)
    return outreal, outimage

inreal = [random.randint(1,8) for i in range(0,128)]
inimage = [0 for i in range(0,128)]
outreal = [0 for i in range(0,128)]
outimage = [0 for i in range(0,128)]

start_time = time.time()
outreal,outimage = dft(inreal,inimage,outreal,outimage)
print ("non-threaded dft took {} seconds".format(time.time() - start_time))

def dft_threading(inreal, inimage, outreal, outimage, start_index, end_index):
    n = len(inreal)
    for i in range(start_index, end_index):
            sumreal = 0
            sumimage = 0
            for t in range(start_index, end_index):
                    angle = float(2 * math.pi * t * i / n);
                    sumreal += float(float(inreal[t]) * float(math.cos(angle)) + float(inimage[t]) * float(math.sin(angle)))
                    sumimage += float(float(-inreal[t]) * float(math.sin(angle)) + float(inimage[t]) * float(math.cos(angle)))
            outreal[i] = float(sumreal)
            outimage[i] = float(sumimage)
    return outreal, outimage

threads = []
start_time = time.time()
for i in range(0,4):
    t = threading.Thread(name="thread%d" % i, target=dft_threading, args=(inreal, inimage, outreal, outimage, int((len(inreal) / 4) * i), int((len(inreal) / 4) * i + (len(inreal) / 4)) if i == 0 else int((len(inreal) / 4) * i + (len(inreal) / 4)) - 1 ))
    t.start()
    threads.append(t)
for t in threads:
    t.join()
print ("threaded dft took {} seconds".format(time.time() - start_time))

