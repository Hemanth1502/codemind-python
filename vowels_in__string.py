s = input()
c = ['a','e','i','o','u','A','E','I','O','U']
d = []
for i in s:
    if i in c:
        d.append(i)
    else:
        continue
e = []
for i in d:
    if i not in e:
        e.append(i)
    else:
        continue
if len(e)>0:
    print(*e)
else:
    print(-1)