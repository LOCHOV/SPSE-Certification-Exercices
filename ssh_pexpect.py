#!/usr/bin/env python3

# Automize ssh login with pexpect

from pexpect import pxssh

i = pxssh.pxssh()
i.login('192.168.1.200','user','pass')  # ip/host, username, password
i.sendline('ls')  
i.prompt()
print(i.before.decode('utf-8'))
