

import json
d='{"name":"goli","rollno":32,"branch":"inft","id":1}'


print(type(d))

s=json.loads(d)

print(s)

print(type(s))


for i in s:
    print(s[i])