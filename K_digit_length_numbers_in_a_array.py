n, m = map(int, input().split())
a = list(map(int, input().split()))
c = []
for i in range(n):
    if a[i]>=0:
        x = str(a[i])
        x1 = list(x)
        k = len(x1)
        if k==m:
            c.append(a[i])
        else:
            continue
    elif a[i]<0:
        x = str(a[i])[1::]
        x1 = list(x)
        k = len(x1)
        if k==m:
            c.append(a[i])
        else:
            continue
    else:
        continue
print(len(c))