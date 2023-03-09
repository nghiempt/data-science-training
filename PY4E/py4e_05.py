import json
import urllib.request as ur
count = 0

url = "https://py4e-data.dr-chuck.net/comments_1746691.json"
uh = ur.urlopen(url)
data= uh.read()

info = json.loads(data)
for item in info["comments"]:
	#print item["count"]
	number = int(item["count"])
	count = count + number
print(count)