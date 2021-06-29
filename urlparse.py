import urllib.parse as up

url='https://24h.pchome.com.tw/store/DGCW13?sort=asc&=123'

result = up.urlparse(url)
print(result)
# scheme = 協定
# netlocation = Domain Name (含port)
# path = 路徑 params = 參數, query=查詢 fragment=片段
print('商品ID：', result.path.split('/')[-1])

print(up.quote('練家麟'))
name = '%E7%B7%B4%E5%AE%B6%E9%BA%9F'
print(up.unquote(name))