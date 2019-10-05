#from webcrawl.bugsmusic import BugsCrawler
from webcrawl.Controller import Controller

if __name__ == '__main__':
    print('a : 국회 크롤링')
    print('b : 벅스')
    print('c : 네이버')
    print('d : 종목')
    print('e : 네이버 주가')
    print('f : 네이버 영화')
    print('f : 네이버 로그인')
    print('0 : 종료')
    flag = input('선택')
    call = Controller()

    call.exec(flag)
