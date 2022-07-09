m, n = map(int, input().split())
a = [list(map(int, input().split())) for i in range(m)]
c = 0
d = 0
for i in range(len(a)):
    x = list(a[i])
    for i in range(len(x)):
        if x[i]%2==0:
            c = c+x[i]
        else:
            d = d+x[i]
print(c, d)