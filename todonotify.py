from datetime import datetime, time
from time import sleep
import os

f=open("file.txt")
x=f.readlines()
for i in x:
    os.system("notify-send %s" %i)
    sleep(360)


