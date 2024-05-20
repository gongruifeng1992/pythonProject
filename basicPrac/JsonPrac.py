import json

# 1-python对象转json
data = [{'a': 1, 'b': 2, 'c': 3}]
data2 = json.dumps(data)
print(data2)
# 2-使用参数让JSON数据格式化输出
data3 = json.dumps({'a': 'runoob', 'b': 7}, sort_keys=True, indent=4, separators=(',', ':'))
print(data3)
# 3-json转python对象
jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
text=json.loads(jsonData)
print(text)
