n, m = map(int, input().split())
a = list(map(int, input().split()))
c = 0
for i in range(len(a)):
    if a[i]>=0:
        x = list(str(a[i]))
        if len(x)==m:
            c = c+1
    else:
        x = list(str(a[i]))
        x = x[1:]
        if len(x)==m:
            c = c+1
print(c)