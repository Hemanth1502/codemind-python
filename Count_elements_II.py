n1, n2 = map(int, input().split())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
c1 = []
for i in a2:
    if i not in a1:
        c1.append(i)
for i in a1:
    if i not in a2:
        c1.append(i)
print(len(set(c1)))