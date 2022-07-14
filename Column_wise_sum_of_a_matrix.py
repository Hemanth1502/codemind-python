m, n = map(int, input().split())
a = [list(map(int, input().split())) for i in range(m)]
s = []
for i in range(n):
    c = []
    for j in range(m):
        c.append(a[j][i])
    s.append(sum(c))
print(*s)