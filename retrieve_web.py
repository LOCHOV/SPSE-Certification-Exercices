#!/usr/bin/env python3

import urllib.request

# Downloads the file to local tmp
thefile, headers = urllib.request.urlretrieve('http://python.org/')
print("Here is the file of the requested web: " + thefile)
# print(headers)




