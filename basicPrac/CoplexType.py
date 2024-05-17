# 1-字符串
import calendar
import operator
import time

var1 = 'Hello World !'
var2 = 'Python Runoob'
print("var1[0]=", var1[0])
print("var2[0]=", var2[0])

print("输出 ：-", var1[6] + 'Runoob')

print("My name is %s and weight is %d kg !" % ('Zara', 10))

# 2-List
list1 = [1, 2, 3, 4, 5]
print(list1[1:2])
list1.append('append')
print(list1)
del list1[-1]
print(list1)

list2 = ['a', 'b']
print(operator.eq(list1, list2))
print(operator.eq(list1, list1))

tuple1 = ('123', 4, 3.0)
print(tuple1)
print(list(tuple1))
list.reverse(list2)
print(list2)

# 3-tuple
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"
tup4 = (4,)  # 只有一个元素，需要逗号分隔
tup5 = tup1 + tup2
print(tup5)

# 4-dict
tinydict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(tinydict['Name'])
print(tinydict['Class'])

try:
    print(tinydict['Sex'])
except KeyError as e:
    print("获取参数异常，", e.args)

print(tinydict.values())

# 5-时间
ticks = time.time()
print("当前时间戳为：", ticks)

localtime = time.localtime(time.time())
print('本地时间为：',localtime)

localtime1 = time.asctime(time.localtime(time.time()))
print('本地时间为：',localtime1)

print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
print(time.strftime("%a %b %d %H:%M:%S %Y",time.localtime()))
a='2024-05-16 16:20:20'
b='Thu May 16 16:20:20 2024'
print(time.mktime(time.strptime(b,"%a %b %d %H:%M:%S %Y")))#字符串转时间戳
print(time.mktime(time.strptime(a,"%Y-%m-%d %H:%M:%S")))#字符串转时间戳

cal=calendar.month(2024,5)
print("以下2024年5月日历：")
print(cal)