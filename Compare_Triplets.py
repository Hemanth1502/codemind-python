a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = 0
d = 0
for i in range(len(a)):
    if a[i]>b[i]:
        c = c+1
    elif a[i]<b[i]:
        d = d+1
    else:
        continue
e = list(str(c))
f = list(str(d))
g = e+f
print(*g)