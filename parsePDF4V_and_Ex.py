import pdfplumber
import re
from wdsAndExps import *
import xlwt

pdf = pdfplumber.open("WPME_Chapter_16_Wds&Exp&LangPoints_stud.pdf")

pattern1=r"(\n\d\. |\n\d\d\. |\n\d\d\d\. | \d\. | \d\d\. | \d\d\d\. )"

pages = pdf.pages
WordList=[]

for p in pages:
    text=p.extract_text()
    # print(text)
    if (re.search(pattern1,text) != None):
        result=re.split(pattern1,text)
    result.pop(0)
    # print(result)
    length=int(len(result)/2)
    # print(length)
    # print(range(0,length))
    for i in range(0,length):
        num=result[i*2+1-1].strip().strip("\n").strip(".")
        word=result[i*2+2-1].strip().strip("\n")
        if("♦" in word):
            word=word[:word.find("♦")]
            wds=wdsAndExps(num,word,"♦")
        elif("▲" in word):
            word=word[:word.find("▲")]
            wds=wdsAndExps(num,word,"▲")
        else:
            wds=wdsAndExps(num,word,"")
        # wds.print()
        WordList.append(wds)
          
wb = xlwt.Workbook()
sh1 = wb.add_sheet('LangPoints解析结果')
sh1.write(0,0,"序号")
sh1.write(0,1,"单词")
sh1.write(0,2,"备注")

i=1
for wds in WordList:
    sh1.write(i,0,wds.num)
    sh1.write(i,1,wds.word)
    sh1.write(i,2,wds.Note)
    i+=1

wb.save('LangPoints解析结果-WPME Chapter 16.xls')