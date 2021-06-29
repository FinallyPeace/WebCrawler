import json

# F-String
name = '台積電'
code = 2330
print('name = %s, code = %d' % (name, code))
# 缺點：遇到證交所把欄位對調，前後都要調
print(f'name = {name}, code = {code}')

# Raw String (原始字串)
print('D:\\name')
# 為了躲跳脫字元多打\
print(r'D:\name')

# List Slice
str = '0123456789'
print(str[2:-2:2])

# List Creation from For Loop
# Object
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
odds = [i for i in num if i % 2 != 0]
print(odds)
# Dictionary
stocks = [{
    'name': '台積電',
    'close': 603
}, {
    'name': '華碩',
    'close': 385
}]
print([
    stock['name']
    for stock in stocks
    if stock['close'] > 500
])

# Search 是否包含
if '123' in str:
    print('substr in String')
if 2 in num:
    print('item in List')
if 'name' in stocks[0]:
    print(f'key in {stocks[0]}')
if '台積電' in stocks[0].values():
    print(f'{stocks[0].values()}')
print(f'{stocks[0].keys()}\n{stocks[0].items()}')


# JSON String to Python List or Dict
s = '{"name": "台積電"}'

data = json.loads(s)
print(data)
print(data['name'])

# Python List or Dict to JSON String
obj = [{
    'name': '華碩'
}]

j = json.dumps(obj, ensure_ascii=False)
print(j)
