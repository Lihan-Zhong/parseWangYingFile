class wdsAndExps(object):
    def __init__(self,num,word,Note):
        self.num=num
        self.word=word
        self.Note=Note
    def print(self):
        print(self.num+'. '+self.word+"\t"+self.Note)