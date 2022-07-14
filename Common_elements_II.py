n1, n2 = map(int, input().split())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
c = []
for i in a1:
    if i not in a2:
        c.append(i)
for i in a2:
    if i not in a1:
        c.append(i)
b = []
for i in c:
    if i not in b:
        b.append(i)
print(*b)