from textMining.model import SamsungReport

if __name__ == '__main__':
    #f = SamsungReport.read_file()
    sam = SamsungReport()
    # sam.download()
    #print(sam.extract_noun())
    #print(sam.read_file())
    #sam.find_freq()
    #print(sam.remove_stopword())
    sam.draw_wordcloud()