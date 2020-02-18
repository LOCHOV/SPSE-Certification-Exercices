#!/usr/bin/env python
from scapy.all import *

for x in range(0, 256):
    ip = '172.19.151.'+str(x)
    arp = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(hwdst='ff:ff:ff:ff:ff:ff', pdst=ip)
    a = srp1(arp, verbose=0, timeout=1)
    if a:
        print(a)
        print(a.psrc + " -> " + a.hwsrc)
    else:
        pass


