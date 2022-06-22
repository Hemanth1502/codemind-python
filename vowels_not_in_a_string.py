n = input()
a = ['a','e','i','o','u']
b = []
for i in n:
    if i in a:
        b.append(i)
    else:
        continue
c = []
for i in a:
    if i not in b:
        c.append(i)
    else:
        continue
if len(c)>0:
    print(*c)
else:
    print(0)