# 抓取網頁原始碼 HTML
import bs4
import urllib.request as req

url = 'https://www.ptt.cc/bbs/movie/index.html'

# 建立 Request 物件 附加 Request Headers 資訊
request = req.Request(url, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
})

with req.urlopen(request) as response:
    data = response.read().decode('utf-8')
# print(data) 印出 HTML

# 讓 BeautifulSoup 解析 HTML
root = bs4.BeautifulSoup(data,"html.parser")
# 找所有 <div class="title">
titles = root.find_all("div",class_="title")

for title in titles:
    if title.a != None:
        print(title.a.string)
