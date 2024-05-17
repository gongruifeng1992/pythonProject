num_int = 100
num_float = 1000.0
str_name = "John"

print(num_int)
print(num_float)
print(str_name)

a=b=c=1
print("a="+str(a),"b="+str(b),"c="+str(c))

#数字
var1 = 1
var2 = 2
print("var1="+str(var1))
# del var1
# print("del后var1="+str(var1))

#字符串
s = "a1a2...an" #n>=0

s = 'abcdef'
print(s[1:5])
str1 = "Hello World"
print(str1)
print(str1[0])
print(str1[2:6])
print(str1[2:])
print(str1*2)
print(str1+" Test")
print(str1[1:4:3])

#列表
list =['runoob',786,2.23,['a','b'],('runoob',123),{'name':'nono','age':12}]
for element in list:
        print(str(element)+"'s type is "+str(element.__class__))

#元组，不允许更新数据
list1 = [1,2]
tuple1 = (1,2)
list1[0]=1000
try:
        tuple1[0]=1000
except Exception  as e:
        print(e)
        print(tuple1[0])