# 条件语句
import math
import operator
from filecmp import cmp
from random import random, uniform, shuffle

flag = False
name = 'nono'
if name == 'python':
    flag = True
    print("Welconme !")
else:
    print(name)

num = 5
if num == 3:
    print('3')
elif num == 2:
    print('2')
elif num == 4:
    print('4')
else:
    print('else 中的 5')

num = 9
if 0 < num < 10:
    print("0<num<10")

if num < 0 or num > 5:
    print('2')

var = 100
if var == 100: print("var=100")
print('Goodbye')

# 循环语句
# 1-while
a = 5
while a < 10:
    print("a = " + str(a))
    a += 1

num = [1, 2, 3, 4, 5]
js = []
os = []
while len(num) > 0:
    numb = num.pop()
    if numb % 2 == 0:
        print(str(numb) + " 是偶数");
        os.append(numb);
    else:
        print(str(numb) + " 是奇数");
        js.append(numb);
print(js, os)

i = 0;
while i < 10:
    print("当前i = " + str(i))
    i += 1
    if i == 5:
        print("skip i=5")
        continue

# var = 1
# while var == 1:
#     num = input("Enter a number :")
#     print("Your num is ", num)
#     if num=='10':
#         break
# print('Goodbye !')

count = 0
while count < 5:
    print(count, "is less than 5")
    count += 1
else:
    print(count, "is equal to 5")

# 2-for
for letter in "sorry":
    print(letter)

fruits = ['apple', 'banana', 'pear']
for fruit in fruits:
    print(fruit)

for index in range(len(fruits)):
    print("index ", fruit)

for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            print(num, "不是质数")
            break
        else:
            print(num, "是质数")
            break
# 3-嵌套循环
i = 2
while i < 10:
    j = 2
    while j <= (i / j):
        if not (i % j): break
        j += 1
    if j > i / j: print(i, "是素数")
    i += 1

# 4-break
for letter in 'pyThon':
    if letter == 'T':
        break
    print(letter)

# 5-continue
var = 10
while var > 0:
    print("var = ", var)
    var -= 1
    if var == 4:
        print("var = 4,brak")
        break

# 6-pass
for letter in 'python':
    if letter == 'h':
        pass
        print('This is pass')
    print('The letter is ', letter)

print("绝对值：",abs(-10))
print("向上取整：",math.ceil(3.22))
print("比较数值:",operator.eq(-1,-1))#3.0使用operator，无cmp函数
print("生成一个0-1随机数：",random())
print("随机生成一个实数：",uniform(2,10))
list_num=[1,2,3,4]
print("原始序列：",list_num)
shuffle(list_num)
print("序列的所有元素随机排序",list_num)


