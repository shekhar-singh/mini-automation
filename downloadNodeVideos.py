import webbrowser
import os

chromedir= "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
# all = os.listdir(".")

all = os.listdir("D:\Users\Default User\Videos\NodeJs")

#open n download all link
with open('Videolinks.txt','r') as f:
    content = f.readlines()
    for i in content:
        webbrowser.get(chromedir).open(i)

#remove empty lines in a file
with open('Videolinks.txt') as infile, open('output.txt', 'w') as outfile:
    for line in infile:
        if not line.strip(): continue  # skip the empty line
        outfile.write(line)

#count links/ lines in file
with open('output.txt','r') as f:
    content = f.readlines()
    for i ,j in enumerate(content,1):
        print [i, ':',j]

list=[]
for i in all:
    if i.endswith('.mp4'):
        list.append(i)

with open('output.txt','r') as f:
    content = f.readlines()
    for i in content:
        if i.split("/")[-1].strip() not in list:
            webbrowser.get(chromedir).open(i)
            

#rough works below
with open('outcom.txt', 'w') as outfile:
    for i in all:
        if i.endswith('.mp4'):
            outfile.write(i+ "\n")
    outfile.close