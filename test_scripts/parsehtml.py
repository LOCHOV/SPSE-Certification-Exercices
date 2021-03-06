#!/usr/bin/env python3

from bs4 import BeautifulSoup
import urllib.request

url = "http://testing-ground.scraping.pro/login"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
print(response.code)

parse = BeautifulSoup(response.read(), "lxml")
# print(parse)  # all content
print(parse.title)  # full title
print(parse.title.string)  # only string
print(parse.title.name)  # only tag name

print(parse.find_all("meta"))  # find all
print("")
print(parse.find_all("meta")[0]["charset"]) # select a specific one as dictionary

print("\n\n------------------------------------\n\n")
print("all links:")
alllinks = parse.find_all("a")
for x in range(len(alllinks)):
    print(alllinks[x]["href"])

print("\n\n------------------------------------\n\n")
# print(parse.get_text())
