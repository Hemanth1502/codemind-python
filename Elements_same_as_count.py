n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n):
    if a[i]==a.count(a[i]):
        b.append(a[i])
c = []
for i in b:
    if i not in c:
        c.append(i)
if len(c)>0:
    print(*c)
else:
    print(-1)