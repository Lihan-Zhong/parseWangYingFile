import pdfplumber
import re
from Root import *
import xlwt

pdf = pdfplumber.open("WPME重点词根.pdf")

pattern1=r"\n\d\)|\n\d\d\) "
pattern2=r"\n\d\. |\n\d\d\. "

pages = pdf.pages
RootList=[]
i=1
for p in pages:
    text=p.extract_text()
    if (re.search(pattern1,text) != None):
        result=re.split(pattern1,text)
    elif (re.search(pattern2,text)!=None):
        result=re.split(pattern2,text)
    # print(result)
    # print()
    for para in result:
        para=para.strip(" ")
        a=("-" in para) | ("–" in para)
        b=(":" in para)
        c=(";" in para)
        if(a&b):
            # print(para)
            sp=re.split(":",para,1)
            rootInfo=sp[0]
            # print(rootInfo)
            spRoot=re.split("–",rootInfo)
            root=spRoot[0].strip().strip("\n")
            meaning=spRoot[1].strip().strip("\n")
            # print(root+":---"+meaning)
            wdListRaw=sp[1]
            wdListInfo=re.split(",|;",wdListRaw)
            wordlist=[]
            for wd in wdListInfo:
                word=wd.strip().strip("\n")
                if len(word)<=3:      #老师的单词一般还是长于3的……
                    continue
                else:
                    wordlist.append(word)
            # print(wordlist)
            # print(wdListInfo)
            rt=Root(root,meaning,wordlist)
            RootList.append(rt)
    print("Page "+str(i))
    i+=1
    # a=[text]
    # print(a)
    # print()
    
wb = xlwt.Workbook()
sh1 = wb.add_sheet('词根解析结果')
sh1.write(0,0,"词根意思")
sh1.write(0,1,"词根")
sh1.write(0,2,"衍生词")

i=1
for rt in RootList:
    sh1.write(i,0,rt.meaning)
    sh1.write(i,1,rt.root)
    for wd in rt.wordlist:
        sh1.write(i,2,wd)
        i+=1
    i+=1

wb.save('词根解析结果.xls')