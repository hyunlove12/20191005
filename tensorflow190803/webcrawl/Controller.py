from webcrawl.bugsmusic import BugsCrawler
from webcrawl.assembly import AssemblyCrawler
from webcrawl.naver import NaverCrawler as nc
from webcrawl.krx import KrxCrawler
from webcrawl.naver_stock import StockModel as sm
from webcrawl.naverMovie import NaveMovieCrawler as nm
from webcrawl.naverLogin import NaverLogin
class Controller:
    def __init__(self):
        pass

    def exec(self, flag):
        if flag == 'a':
            url = 'http://likms.assembly.go.kr/bill/billDetail.do?billId=PRC_R1N9J0N1X0Y9A1O8S3R5Z3J3K9O8N7'
            a = AssemblyCrawler(url)
            a.scrap()
        elif flag == 'b':
            url = 'https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20190810&charthour=11'
            b = BugsCrawler(url)
            b.scrap()
        elif flag == 'c':
            url = 'https://finance.naver.com/sise/'
            c = nc(url)
            c.scrap()
        elif flag == 'd':
            url = "http://kind.krx.co.kr/disclosureSimpleSearch.do?method=disclosureSimpleSearchMain"
            d = KrxCrawler(url)
            d.scrap()
        elif flag == 'e':
            url = ''
            e = sm('005930')
            e.scrap()
        elif flag == 'f':
            url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
            f = nm(url)
            f.scrap()
        elif flag == 'g':
            url = "https://nid.naver.com/nidlogin.login"
            g = NaverLogin(url)
            g.auto_login()
