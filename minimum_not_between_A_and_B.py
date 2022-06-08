n = int(input())
a = list(map(int, input().split()))
x, y = map(int, input().split())
c = []
for i in range(len(a)):
    if a[i]>=x and a[i]<=y:
        c.append(a[i])
    else:
        continue
d = []
for i in a:
    if i not in c:
        d.append(i)
    else:
        continue
if len(d)>0:
    print(min(d))
else:
    print(-1)