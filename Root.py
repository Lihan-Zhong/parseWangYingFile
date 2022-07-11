class Root(object):
    def __init__(self,root,meaning,wordlist):
        self.root=root
        self.meaning=meaning
        self.wordlist=wordlist
    
    def printMeaning(self):
        output=self.root+","+self.meaning
        return output
    
    def print(self):
        print(self.root+self.meaning)