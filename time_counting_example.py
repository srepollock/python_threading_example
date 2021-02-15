#!/usr/bin/env python3

import threading
import os
import sys
import time

def print_time(thread_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print ("%s: %s" % (thread_name, time.ctime(time.time())))

def main():
    threads = [2]
    print("Starting threads")
    thread1 = threading.Thread(target=print_time, kwargs={"thread_name":"Thread-1", "delay":2})
    thread2 = threading.Thread(target=print_time, kwargs={"thread_name":"Thread-2", "delay":4})
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    return 0

if __name__ == "__main__":
    main()

