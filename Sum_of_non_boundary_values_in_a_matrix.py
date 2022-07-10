m, n = map(int, input().split())
x = []
for i in range(m):
    a = list(map(int, input().split()))
    x.append(a)
b = []
for i in range(m):
    c = []
    for j in range(n):
        if i!=0 and i!=m-1:
            if j!=0 and j!=n-1:
                c.append(x[i][j])
    b.append(c)
y = []
for i in range(len(b)):
    y.append(sum(b[i]))
print(sum(y))