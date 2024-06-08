

import json


file = open("/home/shyam/Desktop/Daily_Python_coding_(Dsa)/Revision/simpleproject/last.json", '+r')
x=file.read()

print(type(x))


y=json.loads(x)
print(y)

print(type(y))


for i in y:
    print(i['roll'],i['name'])
