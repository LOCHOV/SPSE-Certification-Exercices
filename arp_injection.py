#!/usr/bin/env python3

import socket
import struct
import binascii


class InjectPacket:
    def __init__(self, packet):
        self.s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0806))
        self.p = packet

    def injection(self):
        self.s.bind(("eth0", socket.htons(0x0800)))
        self.s.send(self.p)
        self.s.close()
        return "arp-request was sent, check wireshark"


def ipformat(ip):
    ip = socket.inet_aton(ip)
    ip_long = struct.unpack("!L", ip)[0]  # IP in long format
    return ip_long


def main():

    """ ARP PACKET DEFINE ALL 9 FIELDS """
    htype = 0x0001  # 2 bytes
    ptype = 0x0800  # 2 bytes
    hlen = 0x0006
    plen = 0x0004
    oper = 0x0001
    sha = binascii.unhexlify("901b0e8f7ead")
    spa = ipformat("0.0.0.0")
    tha = binascii.unhexlify("ffffffffffff")  # broadcast mac
    tpa = ipformat("172.29.101.190")
    arp_packet = struct.pack("!HHBBH6sI6sI", htype, ptype, hlen, plen, oper, sha, spa, tha, tpa)
    print("arp packet: " + arp_packet)

    """ ETHERNET HEADER DEFINE 3 FIELDS """
    destmac = tha
    srcmac = sha
    ethertype = 0x0806
    eth_header = struct.pack("!6s6sH", destmac, srcmac, ethertype)
    print("eth header: " + eth_header)
    full = eth_header + arp_packet
    print("full packet:" + full)

    """ CALL INJECT PACKET FUNCTION"""
    mysock = InjectPacket(full)
    print(mysock.injection())


main()

