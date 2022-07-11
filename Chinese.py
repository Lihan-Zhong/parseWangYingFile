class Chinese(object):
    def __init__(self,character,meaning):
        self.character=character
        self.meaning=meaning
    
    def printMeaning(self):
        output=self.character+self.meaning+"\n"
        output.strip("\n")
        return output[:-1]
    
    def print(self):
        print(self.character+self.meaning)