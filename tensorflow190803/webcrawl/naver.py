from bs4 import BeautifulSoup
import urllib.request as url

class NaverCrawler:
    def __init__(self, param):
        self.param = param

    def scrap(self):
        #html = url.urlopen(self.param).read()
        html = url.urlopen('https://finance.naver.com/item/sise_day.nhn?code=005930').read()

        soup = BeautifulSoup(html, 'html.parser')
        print(soup.find(id='KOSPI_now').text)