import json
import urllib2
import requests
# open the url and the screen name 
# (The screen name is the screen name of the user for whom to return results for)
url = "http://api.twitter.com/1/statuses/user_timeline.json?screen_name=python"

# this takes a python object and dumps it to a string which is a JSON
# representation of that object
data = json.load(urllib2.urlopen(url))

# print the result
print (data)


#post json 
url = "http://ghosting.nl/pygame"

datas = {"name":"6248889874650987","systemIdentify":"s08","sourceChannel": 12}

headers = {'Content-type': 'application/json'}

rsp = requests.post(url, json=datas, headers=headers)