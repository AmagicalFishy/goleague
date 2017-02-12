import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup, SoupStrainer

url = "http://www.usgo.org/ratings-lookup-id?PlayerID=" + str(sys.argv[1])
response = urlopen(url)
table = SoupStrainer('table',{'border': 0, 'cellpadding': 5})
soup = BeautifulSoup(response, "html.parser", parse_only = table)
playerInfo = soup.findAll("td")
tableInfo = soup.findAll("th")

print()
for ii in range(len(playerInfo)):
    print(tableInfo[ii].text + ": " + playerInfo[ii].text)
print()
