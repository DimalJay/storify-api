from newspaper.extractors import PIPE_SPLITTER
import requests
from bs4 import BeautifulSoup
import urllib


def getContent(soup):
    content = ""
    parg = soup.findAll("p")
    for p in parg:
        if(p.text.strip() != ""):
            content += p.text.strip()+"\n"
    return content

def getTitle(soup):
    return soup.find("h1").text

def getThumnailUrl(soup):
    thumbnail = soup.find("img")
    return urllib.parse.urljoin("https://telegra.ph/",thumbnail.attrs["src"])

def getSoup(url):
    html = requests.get(url).text
    return BeautifulSoup(html, features="html.parser")


def getArticle(url):
    soup = getSoup(url)
    title = getTitle(soup)
    content = getContent(soup)
    thumbnail = getThumnailUrl(soup)

    return {"title":title, "content":content, "thumbnail":thumbnail}


urls = [
    "https://telegra.ph/%E0%B6%B8%E0%B6%BD%E0%B6%9A%E0%B6%B8%E0%B6%AF-%E0%B7%80%E0%B6%BA%E0%B6%BA%E0%B6%AD-08-06-15",
    "https://telegra.ph/OPERATION-K--L---15-07-13",
]

def getArticles():
    articles = []
    for url in urls:
        articles.append(getArticle(url))
    return articles
    

