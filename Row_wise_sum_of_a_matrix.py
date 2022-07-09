m, n = map(int, input().split())
a = [list(map(int, input().split())) for i in range(m)]
b = []
for i in range(len(a)):
    c = sum(a[i])
    b.append(c)
print(*b)