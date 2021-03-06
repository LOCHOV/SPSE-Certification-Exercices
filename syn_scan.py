#!/usr/bin/env python
from scapy.all import *

dst_ip = "192.168.1.1"
src_port = RandShort()  # random source port
print("Port scan started on " + dst_ip)
for x in range(1, 1000):
    packet = IP(dst=dst_ip)/TCP(sport=src_port, dport=x, flags="S")
    response = sr1(packet, timeout=2, verbose=0)

    if response.haslayer(TCP):
        if response.getlayer(TCP).flags == 0x12:  # flag 12 stands for SYN ACK
            print("port " + str(x) + " opened")
        else:
            pass

