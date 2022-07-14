n = int(input())
a = list(map(int, input().split()))
b = []
c = []
for i in a:
    if i not in b:
        b.append(i)
for i in range(len(b)):
    c.append(b[i])
    c.append(a.count(b[i]))
print(*c)