n = int(input())
a = list(map(int, input().split()))
b = []
c = 0
for i in range(n):
    x = str(a[i])
    x1 = list(x)
    k = len(x1)
    b.append(k)
mi = min(b)
for i in range(n):
    y = str(a[i])
    y1 = list(y)
    k1 = len(y1)
    if k1==mi:
        c = c+1
    else:
        continue
print(c)