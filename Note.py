class Note(object):
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    
    def printMeaning(self):
        output=self.word+": "+self.meaning+"\n"
        output.strip("\n")
        return output[:-1]
    
    def print(self):
        print(self.word+": "+self.meaning)