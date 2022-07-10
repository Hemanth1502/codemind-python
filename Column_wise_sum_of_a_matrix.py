m, n = map(int, input().split())
x = []
for i in range(m):
    a = list(map(int, input().split()))
    x.append(a)
b = []
for i in range(n):
    c = []
    for j in range(m):
        c.append(x[j][i])
    b.append(c)
y = []
for i in range(len(b)):
    y.append(sum(b[i]))
print(*y)