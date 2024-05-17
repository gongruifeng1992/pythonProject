class Test:
    testParam = 1

    def prt(self):
        print(self.testParam)
        print(self)
        print(self.__class__)


t = Test()
t.prt()
