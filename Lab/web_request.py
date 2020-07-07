import requests

url = 'http://127.0.0.1:5000/login'
data = {'user':'lihongbo','password':'password'}
res = requests.post(url=url,data=data)
for i in res:
    print(i)

