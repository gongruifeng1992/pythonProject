import requests

x=requests.get('https://www.runoob.com/')
print(x.status_code)
print(x.headers)
#print(x.content)
print("是否重定向：",x.is_redirect)
print(x.url)
print(x.reason)
x = requests.get('https://www.runoob.com/try/ajax/json_demo.json')
print(x.json())