# /usr/bin/python3
import sys
import time
import requests
from bs4 import BeautifulSoup

def loading():
    
    sys.stdout.write("\r\\")
    time.sleep(0.3)
    sys.stdout.flush()

    sys.stdout.write("\r|")
    time.sleep(0.3)
    sys.stdout.flush()

    sys.stdout.write("\r/")
    time.sleep(0.2)
    sys.stdout.flush()

    sys.stdout.write("\r")
    time.sleep(0.1)
    sys.stdout.flush()

def cricscore():
    url = "http://static.cricinfo.com/rss/livescores.xml"
    raw_score = requests.get(url)
    data = BeautifulSoup(raw_score.text,"html.parser").find_all("description")

    for index, game in enumerate(data[1:], 1):
        print [ index ,':' , str(game.text) ]

    Choice = int(input("Enter your choice: "))
    if Choice in range(1, index):
        score = data[Choice].text
        print(score)
    else:
        Choice = int(input("Oopss !   Try again : ) "))

try:
    loading()
    cricscore()
except requests.exceptions.ConnectionError:
    print("No Internet Connection :(")
