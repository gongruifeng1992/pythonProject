def testFileIO():
    try:
        fo = open("testfile", "r")
        fo.write("test")
    except Exception as e:
        print("写入异常：", e.__str__())
        fo.close()


testFileIO()


def testFinally():
    try:
        fo = open("testfile", "w")
        fo.write("test")
    finally:
        print("Anyway，need execute")
        fo.close()

testFinally()

def myException(level):
    if level<1:
        raise Exception("Invalid level!")


try:
    myException(0)
except Exception as e:
    print(e)
