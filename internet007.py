import re
import json
from urllib2 import urlopen

data = str(urlopen('http://checkip.dyndns.com/').read())
IP = re.compile(r'(\d+.\d+.\d+.\d+)').search(data).group(1)
url = 'http://ipinfo.io/' + IP + '/json'
response = urlopen(url)
data = json.load(response)

org=data['org']
city = data['city']
ctry=data['country']
reg=data['region']

print org,reg,ctry,city,IP
