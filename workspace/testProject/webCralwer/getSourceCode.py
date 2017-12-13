import urllib.request
import requests

# 下面代码爬取到页面所有信息，css，JavaScript，html等
def getHtml1(url):
    page = urllib.request.urlopen(url)
    html = page.read().decode("utf-8")
    return html

# 爬取到只是html的内容
def getHtml2(url):
    page = requests.get(url)
    page.encoding = 'utf-8'
    return page.text


# url = "http://172.16.50.138"
url = "https://www.zhihu.com/"
try:
    store = open('./getFile/page.txt', 'w', encoding='utf-8')
    store.write(getHtml1(url))
except:
    print("文件处理失败！")
else:
    print("文件写入成功！")
    store.close()