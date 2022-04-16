import requests
import bs4

url = "https://jwglxt1.qust.edu.cn/jwglxt/xtgl/login_slogin.html"

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
a = gethtml(url)

print(a)
ss = bs4.BeautifulSoup(a,"html.parser")

# 找到用户名那一栏
print(ss.find_all("input",attrs={"class":"form-control"}))
# # 找到密码那一栏
# print(ss.find_all("input",attrs={"id":"mm"}))

a = '''<input type="text" class="form-control" name="yhm" id="yhm" value="" placeholder="用户名" onblur="" autocomplete="off">'''