#!/usr/bin/env python3

import threading
import time
import os


def thread_function(arg):  # Function performed by thread 

    child_process = os.fork()  # New process for new thread

    if child_process == 0:  # Only create if process is still nonexistent

        print(threading.currentThread().getName() + " started on pid: " + str(os.getpid()) + " Scan from: " + arg)
        time.sleep(1)
        os.execvp("nmap", ["nmap",arg])  # Perform nmap process on ip


def main():

    ip_range = input("Port-Scan Range: (just number, starting on 127.0.0.1):  ")
    print("Performing portscan from 127.0.0.1 to 127.0.0." + str(ip_range))
    time.sleep(2)
    
    ip_range = round(int(ip_range) / 10)
    ip_start = 1
    for x in range(1,11):  # 10 Threads
        ip_end = ip_range * x
        address_arg = "127.0.0." + str(ip_start) + "-" + str(ip_end)        
        t = threading.Thread(target = thread_function, args = (address_arg,), name = "Thread-ID = " + str(x))  # New threads
        t.start()
        ip_start = ip_end + 1


main()
