import requests
from bs4 import BeautifulSoup
import urllib

from Chinese import *
from Note import Note

url="https://dict.youdao.com/result?word="

def decipherMeaning(meaning):
    if ("&lt;" in meaning):
        meaning=meaning.replace("&lt;","<")
    if ("&gt;" in meaning):
        meaning=meaning.replace("&gt;",">")
    return meaning

class word(object):
    def __init__(self,word):
        print("正在翻译："+word+" ...")
        self.word=word
        self.wordNormalized()
        self.url=url+self.word+"&lang=en"
        self.chinese=self.translate()        
        if (len(self.chinese)==0):
            self.Note()
        else: 
            self.noteList=[]
    
    def translate(self):
        # print(self.url)
        responce=requests.get(self.url)
        soup=BeautifulSoup(responce.text,'html.parser')
        # print(soup.li)
        chineseObj=soup.findAll(name="li",attrs={"class":"word-exp"})
        # print(obj)
        # print(len(obj))
        chinese=self.parseChinese(chineseObj)
        # for chineseObj in chinese:
        #     chineseObj.print()
        return chinese

    def parseChinese(self,obj):
        chineseList=[]
        for ob in obj:
            # print(ob)
            ob=str(ob)
            index1=ob.find("<",5)
            if(ob[index1:index1+3]!="<!-"):
                index2=ob.find(">",index1)+1
                index3=ob.find("</span>",index2)
                character=ob[index2:index3]
            else:
                character=""
                index3=ob.find(">",index1)
            # print(character)
            index1=ob.find(">",index3+len("</span>")+1)
            index2=ob.find("</span>",index1)
            meaning=ob[index1+1:index2]
            meaning=decipherMeaning(meaning)
            # print(meaning)
            wordObj=Chinese(character,meaning)
            chineseList.append(wordObj)
        return chineseList

    def wordNormalized(self):
        newWord=""
        for i in self.word:
            if (i==" "):
                j="%20"
            else :
                j=i
            newWord+=j
        # print(newWord)
        self.word=newWord

    def output_meaning(self):
        out=""
        if (len(self.chinese)>0):
            for obj in self.chinese:
                out=out+obj.printMeaning()+'\n'
        if (len(self.chinese)==0):
            out="未收录 "
        return out[:-1]
    
    def output_Note(self):
        out="您要找的是不是："
        for obj in self.noteList:
            out+=obj.printMeaning()
        return out
    
    def print_Note(self):
        print("您要找的是不是：\n")
        for obj in self.noteList:
            obj.print()

    def Note(self):
        responce=requests.get(self.url)
        soup=BeautifulSoup(responce.text,'html.parser')
        NoteObj=soup.findAll(name="div",attrs={"class":"maybe_word"})
        # print(NoteObj)
        self.noteList=self.parseNote(NoteObj)
    
    def parseNote(self,noteObj):
        # print(noteObj)
        NoteList=[]
        for nt in noteObj:
            # print(nt)
            nt=str(nt)
            index1=nt.find("a class=")
            index2=nt.find(">",index1)
            index3=nt.find("</a>",index2)
            word=nt[index2+1:index3]
            index1=nt.find("p class=",index3)
            index2=nt.find(">",index1)
            index3=nt.find("</p>",index2)
            meaning=nt[index2+1:index3]
            note=Note(word,meaning)
            NoteList.append(note)
        return NoteList

    def print_meaning(self):
        if (len(self.chinese)>0):
            for obj in self.chinese:
                obj.print()
        if (len(self.chinese)==0):
            print("未收录 ")
            if (len(self.noteList)!=0):
                self.print_Note()

# a=word("criminal")
# # a.print_meaning()
# print(a.output_meaning())