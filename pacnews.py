#!/usr/bin/python3
from urllib import request
from bs4 import BeautifulSoup
import sys

class NewsItem:
    def __init__(self, date, msg, author, link):
        self.date = date
        self.msg = msg
        self.author = author
        self.link = link

news = []
printamount = 0

if len(sys.argv) > 1:
    printamount = int(sys.argv[1])

archlinuxnews = "https://www.archlinux.org/news/"

r = request.urlopen(archlinuxnews)
html = r.read()
soup = BeautifulSoup(html, features="html5lib")

table = soup.body.find("table", attrs={"class" : "results", "id" : "article-list"})

for row in table.find("tbody").find_all("tr"):
    item = row.find_all("td")
    n = NewsItem(item[0].text, item[1].text, item[2].text, link=item[1].find("a").get("href"))
    news.append(n)

data = reversed(sorted(news, key=lambda n: n.date))

for i, n in enumerate(data):
    if i > printamount:
        break
    print("{} | {}".format(n.date, n.msg))
