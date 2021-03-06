#!/usr/bin/env python3

import socket
import multiprocessing

def process_func():  
    print("Process: " + str(multiprocessing.current_process()) + " started")
    data = "temp"
    while data != "":
        data = client.recv(4098)
        data = data.decode("utf-8")
        print(data)
        client.send(bytes(data, "utf-8"))
    print("connection left on following process: " + str(multiprocessing.current_process()))


ip = "127.0.0.2"
port = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # To be able to reuse address after program finishes
s.bind((ip, port))
s.listen(10)
print("Serving at: " + str(ip) + ":" + str(port))


while True:
    client, ip = s.accept()
    if client != "":  # Detect when new connection is setup
        print("Connection")
        p = multiprocessing.Process(target = process_func, args = ())  # Start new process for the new connection     
        p.start()

s.close()
