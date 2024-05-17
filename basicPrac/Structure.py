# 1-函数
def printme(str):
    print("The param is: ", str)
    return str


printme("To be No1.")


def ChangeInt(a):  # string tuples number不可变，dict、list可变
    a = 10


b = 2
ChangeInt(b)
print(b)


def ChangeMe1(myList):
    myList.append('append')
    print(myList)
    return


myList = [1, 2, 3]
ChangeMe1(myList)


def ChangeMe2(myDict):
    myDict.pop('name')
    print(myDict)
    return


myDict = {'name': 'nono', 'age': 10}
ChangeMe2(myDict)


def printInfo(name, age=35):  # 打印默认参数
    print(name)
    print(age)
    return


printInfo('nono')
printInfo('yoyo', 18)


def printparams(arg1, *vartuple):  # 不定长参数
    print(arg1)
    for var in vartuple:
        print(var)
    return
printparams('arg1')
printparams(70, 'nono', 2.5)
print("printparams return:",printparams(1))

sum = lambda num1,num2:num1+num2 #匿名函数
print(sum(10,20))

def returnData():
    list1=[1,'3','nono']
    return list1
print(returnData())

# 2-变量作用域
total = 0 #全局变量
def varField():
    total=1 #局部变量
    print(total)

varField()
print(total)
