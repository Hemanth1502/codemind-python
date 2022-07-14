n = int(input())
a = list(map(int, input().split()))
s = []
c = []
for i in range(len(a)):
    x = list(str(a[i]))
    s.append(len(x))
for i in range(len(a)):
    x = list(str(a[i]))
    if len(x)==max(s):
        c.append(a[i])
print(*c)