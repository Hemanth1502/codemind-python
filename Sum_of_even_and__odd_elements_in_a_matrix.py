m, n = map(int, input().split())
a = [list(map(int, input().split())) for i in range(m)]
e = []
o = []
for i in range(len(a)):
    x = a[i]
    for i in range(len(x)):
        if x[i]%2==0:
            e.append(x[i])
        else:
            o.append(x[i])
print(sum(e), sum(o))