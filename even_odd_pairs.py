n = int(input())
a = list(map(int, input().split()))
e = []
o = []
for i in range(len(a)):
    if a[i]%2==0:
        e.append(a[i])
    else:
        o.append(a[i])
if len(e)>len(o):
    for i in range(len(e)-len(o)):
        o.append(0)
else:
    if len(o)>len(e):
        for i in range(len(o)-len(e)):
            e.append(0)
c = []
for i in range(len(e)):
    c.append(e[i])
    c.append(o[i])
for i in c:
    if i==0:
        c.remove(0)
    else:
        continue
if len(c)%2==0:
    print(*c)
else:
    c.append(0)
    print(*c)