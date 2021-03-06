#!/usr/bin/env python3
from bs4 import BeautifulSoup
import urllib.request
import threading
import sys


def retrieve(link_text):
    response_retrieve = urllib.request.urlretrieve("http://localhost/" + link_text)
    return response_retrieve[0]


def nextstep(new_url, depth):
    links = findhref("http://localhost/" + new_url)
    for x in range(len(links)):
        href = links[x].get_attribute_list("href")
        link_text = str(href[-1])
        path = retrieve(link_text)
        print("    ____" + link_text + " -> " + path)
        next = link_text
        if int(depth) >=1:
            depth = int(depth)-1
            nextstep(link_text, depth)


def handler(links, url, x, depth):
    href = links[x].get_attribute_list("href")  # split only href part
    link_text = str(href[-1])  # strip out quotes and parentheses
    path = retrieve(link_text)
    print("____" + link_text + " -> " + path)
    if int(depth) >= 1:
        depth = int(depth)-1
        nextstep(link_text, depth)


def runthread(threads, links, url, x, depth):
    t = threading.Thread(target=handler, args=(links, url, x, depth))
    threads.append(t)
    t.start()
    t.join()


def findhref(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    content = BeautifulSoup(response, "html5lib")
    links = content.find_all("a")
    return links


def main():
    depth = sys.argv[1]
    url = "http://localhost"
    links = findhref(url)
    threads = []
    print("Crawling " + url)
    for x in range(len(links)):
        runthread(threads, links, url, x, depth)


main()