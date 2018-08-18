from bs4 import BeautifulSoup
import requests
import re

url = "https://news.ycombinator.com/newest"

html = requests.get(url)
soup = BeautifulSoup(html.content, 'html.parser')


class article:
    def __init__(self, title, url):
        self.title = title
        self.url = url


def title_lister (soup):
    articles = []
    result = soup.findAll('td', attrs = {'class' : "title"})
    pattern = re.compile(r"\(\w*\.\w*\)")
    result = [something for something in result if re.search(pattern, something.get_text()) is not None]

    #result is cleaned of filth! FILTH!
    for r in result:
        title = r.get_text()[:re.search(pattern, r.get_text()).span()[0]].strip()
        href = r.find('a').get('href')
        articles.append(article(title,href))

    return articles
