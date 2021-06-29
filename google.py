import requests
import urllib.parse as up
import chardet


def search(word):
    word = up.quote(word)
    url = f'https://www.google.com/search?q={word}'

    response = requests.get(
        url,
        headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
        }
    )
    if response.status_code != 200:
        print('request error')
        return

    print(chardet.detect(response.content))

    # 寫檔 wb寫入二進位資料
    # response.text 不同編碼可能拿到亂碼
    # 改用 response.content: binary array
    with open('google.html', 'wb') as f:
        f.write(response.content)

if __name__ == '__main__':
    search('2357')
