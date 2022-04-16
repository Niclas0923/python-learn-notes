import re
import requests

url = "https://www.bilibili.com/v/popular/rank/all"

def gethtml(url):
    fakeheaders = {'User-Agent':'Mozilla/5.0 (windows NT 10.0; Win64; x64)  \
        AppleWebKit/537.36 (KHTML, like Gecko)'  \
        'Chrome/81.0.4044.138 Safari/537.36 Edg/81.0.416.77'}
    
    try:
        r = requests.get(url,headers= fakeheaders)
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        print(e)
        return ""


# 用于获取视频的bv号和名字
m1 = r'\"title\":\"(.+?)\"'
m2 = r'\"bvid\":\"(.+?)\"'


a =gethtml(url)

lst1 = re.findall(m1,a)
lst2 = re.findall(m2,a)

a = []

for i in range(len(lst1)):
    a.append([lst1[i],lst2[i]])

# for i in a:
#     print(i)
ss = open("bilibili_hot.txt","w",encoding="utf8")
for i in a:
    ss.write(i[0]+"\nhttps://www.bilibili.com/video/"+i[1]+"\n")