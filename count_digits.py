n = int(input())
a = list(map(int, input().split()))
c = []
for i in range(n):
    if a[i]>=0:
        x = str(a[i])
        x1 = list(x)
        k = len(x1)
        c.append(k)
    elif a[i]<0:
        x = str(a[i])[1::]
        x1 = list(x)
        k = len(x1)
        c.append(k)
    else:
        continue
print(*c)