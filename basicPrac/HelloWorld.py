# -*- coding: UTF-8 -*-
from __future__ import print_function
print("  *****   ")
print("你好，世界！")
list = ["a","b","c"]
print(list)
print('hello');print('runoob');
if True:
    print('True')
else:
    print('False')
# total = item_1+\
#         item_2+\
#         item+3
days=['Mon','Tues','wedn',
      'Thur','Fri']
print(days)

word = 'word'
sentence = 'sentence'
paragraph = """This is paragraph,
            include many sentences."""
# 单行注释
'''
多行注释，单引号
'''
"""
单行注释，双引号。
"""

#等待用户输入
#input("按下enter键退出，其他任意键显示...\
# n")

x = 'a'
y = 'b'
#换行
print(x)
print(y)
print('-----分割线-----')
#不换行
print(x,y)

list = [2,9,1,0]
for num in  list:
    if num%2==0 and num!=0:
        print(str(num)+"是一个偶数")
    elif num==0:
            print("0既不是奇数，也不是偶数")
    else:
        print(str(num)+"是一个奇数")
