n = int(input())
a = list(map(int, input().split()))
c = 0
b = []
for i in range(n):
    if a[i]>=0:
        x = len(list(str(a[i])))
        b.append(x)
    elif a[i]<0:
        y = list(str(a[i]))
        y1 = y[1:]
        x = len(y1)
        b.append(x)
print(*b)