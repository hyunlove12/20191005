from bs4 import BeautifulSoup
from selenium import webdriver

class NaveMovieCrawler:
    def __init__(self, url):
        # 역 슬래쉬 2개 혹은 슬래쉬 하나
        self.driver = webdriver.Chrome(executable_path='C:/Users/ezen/PycharmProjects/tensorflow190803/webcrawl/data/chromedriver')
        self.driver.get(url)
        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')

    def scrap(self):
        html = self.soup.prettify()
        print(html)
        all_divs = self.soup.find_all('div', attrs={'class':'tit3'})
        print(all_divs)
        arr = [div.a.string for div in all_divs]
        for i in arr:
            print(i)
        self.dirver.close()