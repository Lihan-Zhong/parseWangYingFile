from Translation import *
import xlwt

# wordlist=[]
f = open("sample.txt",encoding='UTF-8')
wordlist=f.readlines()
f.close

newWordlist=[]
for wd in wordlist:
    if "\n" in wd:
        nwd=wd.replace("\n","")
    else:
        nwd=wd
    newWordlist.append(nwd)

wordlist=newWordlist
# print (wordlist)

wb = xlwt.Workbook()
sh1 = wb.add_sheet('翻译结果')
resultList=[]
i=1
sh1.write(0,0,"单词")
sh1.write(0,1,"翻译结果")
sh1.write(0,2,"备注")
for wd in wordlist:
    result=word(wd)
    resultList.append(result)
    sh1.write(i,0,wd)
    sh1.write(i,1,result.output_meaning())
    if (len(result.noteList)!=0):
        sh1.write(i,2,result.output_Note())
    i+=1

wb.save('Result.xls')

