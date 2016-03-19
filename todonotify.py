from datetime import datetime, time
from time import sleep
import os
try:
    f=open("file.txt")
    x=f.readlines()
    for i in x:
        os.system("notify-send %s" %i)
        sleep(360)
except IOError:
   print "Error: can\'t find file or read data"



