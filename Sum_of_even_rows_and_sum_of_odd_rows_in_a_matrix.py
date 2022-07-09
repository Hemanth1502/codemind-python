m, n = map(int, input().split())
a = [list(map(int, input().split())) for i in range(m)]
o = []
e = []
for i in range(len(a)):
    if i%2==0 or i==0:
        c = sum(a[i])
        e.append(c)
    else:
        c = sum(a[i])
        o.append(c)
o1 = sum(o)
e1 = sum(e)
print(e1, o1)