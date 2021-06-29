from bs4 import BeautifulSoup
import urllib.request as ur
import urllib.parse as up


def GSP(word, page):
    word = up.quote(word)
    url = f'https://www.ptt.cc/bbs/Gossiping/search?page={page}&q={word}'

    request = ur.Request(url, headers={
        'Cookie': 'over18=1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    })

    with ur.urlopen(request) as response:
        data = response.read().decode('utf-8')

    root = BeautifulSoup(data, "html.parser")
    articles = root.find_all("div", class_="r-ent")
    recommendations = root.find_all("div", class_="nrec")
    titles = root.find_all("div", class_="title")
    num = []
    list = []
    index = 0

    for recommendation in recommendations:
        index += 1
        span = recommendation.find('span')
        if span is not None:
            if span.string == '爆':
                num.append(index)
    index = 0
    for title in titles:
        index += 1
        if title.a != None:
            if index in num:
                list.append(title.a.string)

    for l in list:
        print(l)


if __name__ == '__main__':
    page = 1
    while page <= 20:
        GSP('爆卦', page)
        page += 1
