#!/usr/bin/env python

# Get all data from file

import os
import sys
import stat 
import time # to change linux time to normal

file_input = sys.argv[1]

data = os.stat(file_input)

# The stats:

file_name = file_input
file_size = data[stat.ST_SIZE]
file_creation = time.strftime("%m/%d/%Y %I:%M:%S %p", time.localtime(data[stat.ST_CTIME]))

print(file_name)
print(file_size)
print(file_creation)

