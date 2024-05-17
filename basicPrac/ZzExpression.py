# 1-re.match
import re

print(re.match('www','www.baidu.com').span()) #在其实位置匹配
print(re.match('com','www.baidu.com')) #不在起始位置匹配

phone = "2004-959-559 # 这是一个国外电话号码"

# 删除字符串中的 Python注释
num = re.sub(r'#.*$', "", phone)
print("电话号码是: ", num)

# 删除非数字(-)的字符串
num = re.sub(r'\D', "", phone)
print("电话号码是 : ", num)