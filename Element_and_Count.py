n = int(input())
a = list(map(int, input().split()))
b = []
for i in a:
    if i not in b:
        b.append(i)
    else:
        continue
c = []
for i in range(len(b)):
    c.append(b[i])
    d = a.count(b[i])
    c.append(d)
print(*c)