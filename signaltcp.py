#!/usr/bin/env python3

import socket
import sys
import signal

ip = "127.0.0.2"
port = 7780
time = sys.argv[1]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, port))
s.listen(10)
signal.alarm(int(time))

print("Listening on: " + ip + ":" + str(port))
while True:
    conn, addr = s.accept()
    print("thanks for connecting")
    
        

    
    


