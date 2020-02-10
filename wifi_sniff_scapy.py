#!/usr/bin/env python3
from scapy.all import *

print("go")


def callback(packet):
    print("ok")
    if packet.haslayer(Dot11):
        if packet.type == 0 and packet.subtype == 8:
            print(packet.info.decode("utf-8"))
            print(packet.addr2)


pack = sniff(iface='Wi-Fi', prn=callback)

