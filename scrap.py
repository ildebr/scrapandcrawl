import requests, sys, webbrowser, bs4,csv

linkFetched = 'https://github.com/joyoyoyoyoyo/lamport-logical-clocks-in-a-distributed-system'
def fetchPage():
    res = requests.get(linkFetched)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    return soup

soup = fetchPage()

def guardarElementos():
    
    title = soup.findAll("a", {"data-pjax" : "#repo-content-pjax-container"})
    readme = soup.findAll("pre", {"style": "white-space: pre-wrap"})
    author = soup.findAll("a", {"rel": "author"})

    lang = soup.findAll("span", {"class", "color-fg-default text-bold mr-1"})
    watch = soup.select("div.mt-2 a.Link--muted strong")
    pack = soup.select(".BorderGrid-row .BorderGrid-cell .text-small.color-fg-muted")


    f = open("act2t3.csv", "a", newline="")
    writer = csv.writer(f)
    writer.writerow(("link fetched: ", linkFetched))
    print(("title", title[0].text))
    writer.writerow(("title", title[0].text))
    writer.writerow(("readme", readme[0].text))
    writer.writerow(("author", author[0].text))

    for l in lang:
        writer.writerow(("language", l.text))

    writer.writerow(("Estrellas", watch[0].text))
    writer.writerow(("Vistas", watch[1].text))
    writer.writerow(("forks", watch[2].text))

    writer.writerow(("Releases", pack[0].text))
    writer.writerow(("Packages", pack[1].text))

    f.close()

guardarElementos()