n = int(input())
a = list(map(int, input().split()))
b = []
for i in a:
    if i not in b:
        b.append(i)
    else:
        continue
c = []
for i in b:
    k = a.count(i)
    if k==1:
        c.append(i)
    else:
        continue
if len(c)>0:
    print(*c)
else:
    print(-1)