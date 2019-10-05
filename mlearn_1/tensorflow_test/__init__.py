from tensorflow_test.mammal import Mammal
from tensorflow_test.word_sequence import WordSequence
from tensorflow_test.naive_bayes import NaiveBayes
from tensorflow_test.web_crawler import WebCrawler
from tensorflow_test.mail_checker_ctrl import MailCheckerController
if __name__ == '__main__':
    #t = Mammal()
    #t.execute()
    #WordSequence.execute()
    #t = WebCrawler.create_model()
    #nb = NaiveBayes()
    #nb.train('./data/review_train.csv') #기존 리뷰를 분석하여 긍정, 부정을 판단하는 방법을 공부
    #print(nb.classify('내 인생에서 쓰레기 같은 영화')) #이 리뷰는 좋은 리뷰가 아니야라고 판단하는 것 1이 좋은것
    #print(nb.classify('내 인생최고의 영화'))  # 이 리뷰는 좋은 리뷰가 아니야라고 판단하는 것 1이 좋은것

    ctrl = MailCheckerController()
    ctrl.run()
