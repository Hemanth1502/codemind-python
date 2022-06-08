n = int(input())
a = list(map(int, input().split()))
x, y = map(int, input().split())
c = []
for i in range(len(a)):
    if a[i]>=x and a[i]<=y:
        c.append(a[i])
    else:
        continue
if len(c)>0:
    print(min(c))
else:
    print(-1)