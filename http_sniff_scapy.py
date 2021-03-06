#!/usr/bin/env python3
from scapy.all import *
print("go")


def header(packet):
    src_ip = packet[IP].src
    dst_ip = packet[IP].dst
    payload = packet[TCP].payload

    try:
        if payload:  # only interested in not empty requests
            print("\n\n--------------------------------------------------\n\n"
                  "src: " + src_ip +
                  " dst: " + dst_ip +
                  "\npayload: " + str(bytes(payload).decode("utf-8").strip())
                  )
    except UnicodeDecodeError:  # sometimes decoding the bytes does not work
        pass


packets = sniff(iface='Ethernet', prn=header, filter="tcp port 80")

