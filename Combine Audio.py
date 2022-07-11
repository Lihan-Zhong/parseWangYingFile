from moviepy.editor import *
from pydub import AudioSegment
import time
from getMP3 import *

# audio1 = AudioFileClip("Audio Input\misanthrope.mp3").coreader()
# audio2 = audio1.volumex(0)
# audio2.write_audiofile("2s blank.mp3")
# audio1.close()
# AudioSegment.converter=r"D:\Program Files\ffmpeg-n5.0-latest-win64-gpl-5.0\bin\ffmpeg.exe"
# AudioSegment.ffprobe=r"D:\Program Files\ffmpeg-n5.0-latest-win64-gpl-5.0\bin\ffprobe.exe"

# print (AudioSegment.converter)
# print (AudioSegment.ffprobe)

in2sBlank=AudioSegment.from_mp3("2s blank.mp3")
in1sBlank=AudioSegment.from_mp3("1s blank.mp3")

def combine2audio(audio1,audio2):
    inMP3_1=AudioSegment.from_mp3(audio1)
    inMP3_2=AudioSegment.from_mp3(audio2)
    in2sBlank=AudioSegment.from_mp3("2s blank.mp3")
    outMP3=inMP3_1+in2sBlank+inMP3_2
    return outMP3

def outputInOrder4Dictation(wordlist,name):
    print("正在顺序合并音频（泛听用）...")
    wdPath1="Audio Input/"+wordlist[0]+".mp3"
    print("提取音频文件："+wdPath1+"...")
    outputMP3=AudioSegment.from_mp3(wdPath1)
    print("成功！")
    for wd in wordlist[1:]:
        wdpath="Audio Input/"+wd+".mp3"
        print("提取音频文件："+wdpath+"...")
        try:
            wdMp3=AudioSegment.from_mp3(wdpath)
        except Exception as e:
            print("解析异常，正在重新下载mp3文件...")
            print("正在下载...")
            wdObj=word(wd,type=1)
            time.sleep(2)
            print("重新下载完成！")
            try:
                print("重新解析文件："+wdpath+"...")
                wdMp3=AudioSegment.from_mp3(wdpath)
            except Exception as e:
                print("仍然异常，忽略该音频")
            continue
        finally:
            outputMP3=outputMP3+in2sBlank+wdMp3
            print("成功！")

    print("正在保存...")
    outputPath="Audio Output/"+name+".mp3"
    outputMP3.export(outputPath,format='mp3')
    # return outputMP3

def outputInOrder4Listening(wordlist,name):
    print("正在顺序合并音频（泛听用）...")
    wdPath1="Audio Input/"+wordlist[0]+".mp3"
    print("提取音频文件："+wdPath1+"...")
    try:
        outputMP3=AudioSegment.from_mp3(wdPath1)
    except Exception as e:
        print("解析异常，正在重新下载mp3文件...")
        print("正在下载...")
        wdObj=word(wordlist[0],type=1)
        time.sleep(1)
        print("重新下载完成！")
        try:
            print("重新解析文件："+wdPath1+"...")
            wdMp3=AudioSegment.from_mp3(wdPath1)
        except Exception as e:
            print("仍然异常，忽略该音频")
    finally:
        print("成功！")
    for wd in wordlist[1:]:
        wdpath="Audio Input/"+wd+".mp3"
        print("提取音频文件："+wdpath+"...")
        try:
            wdMp3=AudioSegment.from_mp3(wdpath)
        except Exception as e:
            print("解析异常，正在重新下载mp3文件...")
            print("正在下载...")
            wdObj=word(wd,type=1)
            time.sleep(1)
            print("重新下载完成！")
            try:
                print("重新解析文件："+wdpath+"...")
                wdMp3=AudioSegment.from_mp3(wdpath)
            except Exception as e:
                print("仍然异常，忽略该音频")
            continue
        finally:
            outputMP3=outputMP3+in1sBlank+wdMp3
            print("成功！")

    print("正在保存...")
    outputPath="Audio Output/"+name+".mp3"
    outputMP3.export(outputPath,format='mp3')

if __name__ == "__main__":
    f = open("AudioOutputList.txt",encoding='UTF-8')
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
    # wdPathList=[]
    for wd in wordlist:
        wdPath="Audio Input/"+wd+".mp3"
        # wdPathList.append(wdPath)
        if not os.path.exists(wdPath):
            print(wd+".mp3 not exist!")
            print("Now downloading "+wd+"...")
            wdObj=word(wd)
            # wdObj.getMp3()
            print("Success!")
        else:
            print(wd+".mp3 exist!")
    
    sublist=[wordlist[i:i+10] for i in range(0,len(wordlist),10)]
    # print(sublist)
    i=15
    for sub in sublist:
        i+=1
        outputInOrder4Dictation(sub,"12000+ Unit4 "+"chapter "+str(i)+" 顺序音频（听写用）")

    # outputInOrder4Dictation(wordlist,"12000+ Unit5 顺序音频（听写用）")
    # outputInOrder4Listening(wordlist,"12000+ Unit3 顺序音频（泛听用）")

    # combine2audio("blasphemy.mp3","enmity.mp3")
