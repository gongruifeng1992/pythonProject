# 1-re.match
import re

import jsonpath

print(re.match('www', 'www.baidu.com').span())  # 在其实位置匹配
print(re.match('com', 'www.baidu.com'))  # 不在起始位置匹配

phone = "2004-959-559 # 这是一个国外电话号码"

# 删除字符串中的 Python注释
num = re.sub(r'#.*$', "", phone)
print("电话号码是: ", num)

# 删除非数字(-)的字符串
num = re.sub(r'\D', "", phone)
print("电话号码是 : ", num)

# JsonPath
strJson = {"store": {
    "books": [{"name": "我的阿勒泰", "author": "李娟", "price": 10}, {"name": "商事街", "author": "萧红", "price": 20},
              {"name": "撒哈拉的沙漠", "author": "三毛"}]}}
store1 = jsonpath.jsonpath(strJson, '$.store')
print(store1)
store2 = jsonpath.jsonpath(strJson, '$.*')
print(store2)
books = jsonpath.jsonpath(strJson, '$.store.books')
print(books)
title = jsonpath.jsonpath(strJson, '$.store.books[*].name')
print(title)
title1 = jsonpath.jsonpath(strJson, '$..name')
print(title1)
title2 = jsonpath.jsonpath(strJson, '$.store.books[0]')
print(title2)
title3 = jsonpath.jsonpath(strJson, '$.store.books[(@.length-1)]')
print(title3)
title4 = jsonpath.jsonpath(strJson, '$.store.books[0,2]')
print(title4)
title5 = jsonpath.jsonpath(strJson, '$.store.*..price')
print(title5)
title6 = jsonpath.jsonpath(strJson, '$..books[?(@.price)]')
print("----", title6)
title7 = jsonpath.jsonpath(strJson, '$..books[?(@.price>10)]')
print(title7)
title8 = jsonpath.jsonpath(strJson, '$..books[?("撒哈拉" in @.name)]')
print(title8)
title9 = jsonpath.jsonpath(strJson, '$.[0]')
print(title9)

# jsonpath 语法
# 1 $:根节点
# 2 .:访问属性，获取子节点
# 3 ..:表示所有符合条件的内容
# 4 []:访问数组元素，表示迭代器的标示
# 5 [,]：表示多个结果的选择
# 6 [*]：通配符，匹配任何属性或数组元组，代表所有的元素节点
# 7 @：当前节点
# 8 ?()：表示过滤操作
# 9 $.property：访问json对象的属性值
# 10 $[index]：访问JSON数组的元素值
# 11 $.property[index]：访问JSOn对象中的数组元素
# 12 $.property[*]：访问JSon对象中的所有数组元素
# 13 $.property.*：访问JSon对象中的所有子属性
# 14 $.property1.property2:访问Json对象中的嵌套属性

# 正则表达式
# 1- re.match(pattern,string,flags=0)
line = "Cats are smarter than dogs";
matchObj = re.match(r'dogs', line, re.M | re.I)
if matchObj:
    print("match --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")

# 2-re.search(pattern,string,flags=0)
matchObj = re.search(r'dogs', line, re.M | re.I)
if matchObj:
    print("search --> searchObj.group() : ", matchObj.group())
else:
    print("No match!!")

# 3-re.sub(pattern, repl, string, count=0, flags=0)
phone = "2004-959-559 # 这是一个国外电话号码"
num = re.sub(r'#.*$', "", phone)
print("电话号码是: ", num)
num = re.sub(r'\D', "", phone)
print("电话号码是 : ", num)

# 4-re.compile(pattern[, flags])
# pattern : 一个字符串形式的正则表达式
# flags : 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：
#         re.I 忽略大小写
#         re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
#         re.M 多行模式
#         re.S 即为 . 并且包括换行符在内的任意字符（. 不包括换行符）
#         re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
#         re.X 为了增加可读性，忽略空格和 # 后面的注释
pattern = re.compile(r'\d+')
m = pattern.match("one12twothree34four")
print("是否以数字开头：", m)
m = pattern.match('one12twothree34four', 2, 10)
print("从index[2] 开始匹配：", m)
m = pattern.match('one12twothree34four', 3, 10)
print("从index[3] 开始匹配：", m)

# 1-group([group1, …]):方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 group() 或 group(0)；
# 2-start([group]):方法用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为 0；
# 3-end([group]):方法用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0；
# 4-span([group]):方法返回 (start(group), end(group))
pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)
m = pattern.match('Hello World Wide Web')
print(m)
pattern1 = re.compile(r'[a-z]+', re.I)
m1 = pattern1.match('Hello World Wide Web')
print(m1)
print(m.group(0))
print(m.span(0))
print(m.group(2))
print(m.span(2))
print(m.groups())

# 5-findall(string[, pos[, endpos]])
# string : 待匹配的字符串。
# pos : 可选参数，指定字符串的起始位置，默认为 0。
# endpos : 可选参数，指定字符串的结束位置，默认为字符串的长度。

pattern = re.compile(r'\d+')
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)
print(result1)
print(result2)

result = re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10')
print(result)

# 6-re.finditer(pattern, string, flags=0)
it = re.finditer(r"\d+","12a32bc43jf3")
for match in it:
    print (match.group() )

# 7-re.split(pattern, string[, maxsplit=0, flags=0])
# maxsplit：分隔次数，默认为0，不限制次数
print(re.split('\W+', 'runoob, runoob, runoob.'))
print(re.split('(\W+)', ' runoob, runoob, runoob.') )
print(re.split('\W+', ' runoob, runoob, runoob.', 1))

# 8-正则表达式修饰符
# re.I:使匹配对大小写不敏感
# re.L:做本地化识别（locale-aware）匹配
# re.M:多行匹配，影响 ^ 和 $
# re.S:使 . 匹配包括换行在内的所有字符
# re.U:根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
# re.X:该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。

# 9-特殊字符类
# .:匹配除 "\n" 之外的任何单个字符。要匹配包括 '\n' 在内的任何字符，请使用象 '[.\n]' 的模式。
# \d:匹配一个数字字符。等价于 [0-9]。
# \D:匹配一个非数字字符。等价于 [^0-9]。
# \s:匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。
# \S：匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。
# \w:匹配包括下划线的任何单词字符。等价于'[A-Za-z0-9_]'。
# \W：匹配任何非单词字符。等价于 '[^A-Za-z0-9_]'。