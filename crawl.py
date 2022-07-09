import requests, sys, webbrowser, bs4,csv
linkFetched = 'https://google.com/search?q=leslie+lamport'
res = requests.get(linkFetched)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkE = soup.select('div#main > div > div > div > a')
print(linkE)
linkToOpen = min(5, len(linkE))
f = open("act2t2.csv", "a", newline="")
writer = csv.writer(f)
writer.writerow(("link fetched: ", linkFetched))
for i in range(linkToOpen):
    writer.writerow(("link", linkE[i].get('href')))
    webbrowser.open('https://google.com'+linkE[i].get('href'))
f.close()