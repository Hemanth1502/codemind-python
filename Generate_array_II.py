n = int(input())
a = list(map(int, input().split()))
b = []
c = []
for i in range(n):
    if i%2==0:
        b.append(a[i])
    else:
        c.append(a[i])
d = []
for j in range(len(b)):
    for k in range(c[j]):
        d.append(b[j])
print(*d)