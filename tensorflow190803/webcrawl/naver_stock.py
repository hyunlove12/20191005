from bs4 import BeautifulSoup
from urllib.request import urlopen as uo

class StockModel:
    def __init__(self, item):
        self.item = item
        pass

    def scrap(self):
        url = 'https://finance.naver.com/item/sise_day.nhn?code={item}'.format(item=self.item)
        uo(url)
        #class = tah p11
        soup = BeautifulSoup(uo(url), "html.parser")
        for i in soup.find_all(name="span", attrs=({"class":"tah"})):
            print(str(i.text))