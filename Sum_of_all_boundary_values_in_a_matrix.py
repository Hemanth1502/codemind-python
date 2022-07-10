m, n = map(int, input().split())
x = []
for i in range(m):
    a = list(map(int, input().split()))
    x.append(a)
b = []
for i in range(m):
    c = []
    for j in range(n):
        if i==0 or j==0 or j==n-1 or i==m-1:
            c.append(x[i][j])
    b.append(c)
y = []
for i in range(len(b)):
    y.append(sum(b[i]))
print(sum(y))