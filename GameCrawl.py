import requests
import sys
import re
from time import sleep as wait

if len(sys.argv) <= 1:
	sys.exit("{*} Usage: ./GameCrawler.py [int] Depth, [String] sortToken")
else:
	LegacyScan = False
	

data = ""
games = {}
gameIds = {}
result = ""
sortToken = ""

for i in sys.argv:
	if "sortToken" in i:
		sortToken = i.replace("sortToken=", "")
for i in range(int(sys.argv[1])):
	rr = requests.request("GET", "https://games.roblox.com/v1/games/list?" + sortToken + "&startRows=60&maxRows=60&hasMoreRows=true&sortPosition=" + str(i) + "&pageContext.pageId=c6759516-f73a-400c-9089-e0d2cd7a2186&pageContext.isSeeAllPage=true")
	if ("creatorId" in rr.text) == False:
		sys.exit("(*) Sort token invalid!")
	data = data + rr.text
	wait(0.2)

print("(*) data length = " + str(len(data)))
games = re.findall("\"name\":\"[^,]+", data)
gameIds = re.findall("\"placeId\":[^,]+", data)

for i in range(len(games)):
	result += games[i]
	result += gameIds[i]
	result += "\n"

print(result)