x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
count = 0
c = []
for i in a:
    if i not in c:
        c.append(i)
    else:
        continue
d = []
for i in b:
    if i not in d:
        d.append(i)
    else:
        continue
e = []
for i in c:
    if i not in d:
        e.append(i)
    else:
        continue
for i in d:
    if i not in c:
        e.append(i)
    else:
        continue
print(len(set(e)))