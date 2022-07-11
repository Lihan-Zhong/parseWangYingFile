from importlib.machinery import WindowsRegistryFinder
import requests
from bs4 import BeautifulSoup
import urllib.request
import os


url="http://dict.youdao.com/dictvoice?type=0&audio="
url2="http://dict.youdao.com/dictvoice?type=1&audio="

class word(object):
    def __init__(self,word,type=0):
        print("正在解析音频："+word+" ...")
        self.word=word.lower()
        self.wordNormalized()
        if type is 0:
            self.url=url+self.newWord
        if type is 1:
            print("英式发音版本...")
            self.url=url2+self.newWord
        self.mp3=self.getMp3()        
    
    def wordNormalized(self):
        newWord=""
        for i in self.word:
            if (i==" "):
                j="%20"
            else :
                j=i
            newWord+=j
        # print(newWord)
        self.newWord=newWord

    def getMp3(self):
        self.filename="Audio Input/"+self.word+".mp3"
        print("正在下载音频... "+self.filename)
        urllib.request.urlretrieve(self.url, filename=self.filename)
        if os.path.exists(self.filename):
            # 存在这个mp3
            print("下载音频成功："+self.word)
        else:
            # 不存在这个MP3，返回none
            print("下载音频失败："+self.word)

if __name__ == "__main__":
    # wd=word("misanthrope")
    # wd.getMp3()
    # f = open("AudioList.txt",encoding='UTF-8')
    # wordlist=f.readlines()
    # f.close
    # newWordlist=[]
    # for wd in wordlist:
    #     if "\n" in wd:
    #         nwd=wd.replace("\n","")
    #     else:
    #         nwd=wd
    #     newWordlist.append(nwd)

    # wordlist=newWordlist
    # for wd in wordlist:
    #     filename="Audio Input/"+wd+".mp3"
    #     if os.path.exists(filename):
    #         # 存在这个mp3
    #         print(filename+" has existed")
    #         continue
    #     else:
    #         print("Downloading "+wd+" ...")
    #         wdObj=word(wd)
    #         # wdObj.getMp3()
    word("callous",type=1)