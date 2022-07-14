n1, n2 = map(int, input().split())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
c = []
for i in a1:
    if i in a2:
        c.append(i)
for i in a2:
    if i in a1:
        c.append(i)
print(len(set(c)))