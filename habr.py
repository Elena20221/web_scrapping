import re
import requests
import bs4


class Habr:
    def __init__(self):
        self.base_url = 'https://habr.com'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15'
        }

    def parser(self, url):
        self.response = requests.get(self.base_url + url, headers=self.headers)
        self.text = self.response.text
        self.soup = bs4.BeautifulSoup(self.text, features="html.parser")
        return self.soup

    def preview_info(self, key_words):
        articles = self.parser('/ru/all/').find_all('article')
        for article in articles:
            key_list = re.findall(r'\w+', article.find(class_="tm-article-body tm-article-snippet__lead").text, re.I)
            if set(key_list) & set(key_words):
                date = article.find(class_="tm-article-snippet__datetime-published").find("time").attrs['title']
                title = article.find("h2").find("span").text
                href = article.find(class_="tm-article-snippet__title-link").attrs["href"]
                res = f'<{date}>-<{title}>-<{self.base_url + href}>'
                print(res)

    def article_text(self, key_words):
        articles = self.parser('/ru/all/').find_all('article')
        for article in articles:
            href = article.find(class_="tm-article-snippet__title-link").attrs["href"]
            text = re.findall(r'\w+', self.parser(href).find(id="post-content-body").text, re.I)
            if set(text) & set(key_words):
                date = article.find(class_="tm-article-snippet__datetime-published").find("time").attrs['title']
                title = article.find("h2").find("span").text
                res = f'<{date}>-<{title}>-<{self.base_url + href}>'
                print(res)