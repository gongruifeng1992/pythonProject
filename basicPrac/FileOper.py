# str = input("Please Input:")
# print("What you input is: ",str)
import os

fo = open("foo.txt","w")
print(fo.name)
print(fo.closed)
fo.close()
print(fo.closed)
print(fo.mode)

fo = open("foo.txt","w")
position = fo.tell()
print("positon:",position)
fo.write('123\n456\n789')
fo.close()
fo = open("foo.txt","r")
#print(fo.read())
print(fo.read(5))
fo.close()

os.rename('foo.txt','final.txt')

os.mkdir("testDir")
os.rmdir("testDir")

print(os.getcwd())
os.chdir("/Users/jijia/PycharmProjects/pythonProject")
print(os.getcwd())

