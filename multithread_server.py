#!/usr/bin/env python3

import socket
import threading
import select


def thread_func():
    threadName = threading.currentThread().getName()
    print("Thread " + threadName + " started")
    data = "temp"
    while data != "":
        data = client.recv(4098)  # receive the clients message
        data = data.decode("utf-8")  
        print(threadName + ": " + data)            
        client.send(bytes(data, "utf-8"))  # echo back the clients message
    print("Connection on thread " + threadName + " left")


ip = "127.0.0.7"
port = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # reuse same ip address after socket closes
s.bind((ip, port))

print("Serving at: " + str(ip) + ":" + str(port))
count = 0  # counter to name the Threads  
while True:
    s.listen(5)
    count += 1
    client, ip = s.accept()
    if client != "":  # detect a new incoming connection
        print("Connection")
        t = threading.Thread(target = thread_func, args = (), name = count)  # Create new thread for new connection 
        t.start()
       
s.close()
