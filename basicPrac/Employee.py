# 1-类和对象
class Employee:
    emCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emCount += 1

    def displayCount(self):
        print("Total Employee %d " % Employee.emCount)

    def displayEmployee(self):
        print("Name:", self.name, ",Salary:", self.salary)


employee1 = Employee('nono', 10000)
employee1.displayEmployee()
employee1.displayCount()
print("--------------------------------------")
employee2 = Employee('yoyo', 3000)
employee2.displayEmployee()
employee2.displayCount()
print("--------------------------------------")
print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)

print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)


# 2-继承
class Parent:
    parentArr = 100

    def __init__(self):
        print("调用父类构造函数")

    def parentMethod(self):
        print("调用父类方法")

    def setAttr(self, attr):
        Parent.parentArr = attr

    def getAttr(self):
        print("父类属性：", Parent.parentArr)


class Child(Parent):
    def __init__(self):
        print("调用子类构造方法")

    def childMethod(self):
        print("调用子类方法")


child = Child()
child.childMethod()
child.setAttr(90)
child.getAttr()


# 3-重写
class Parent1:
    def myMethod(self):
        print("调用父类方法")


class Child1(Parent1):
    def myMethod(self):
        print("调用子类方法")


c = Child1()
c.myMethod()


# 4-运算符重载
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)


# 5-类的属性与方法
class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公有变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
# print(counter.__secretCount) #报错，不能访问
