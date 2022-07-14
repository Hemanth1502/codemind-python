m, n = map(int, input().split())
a = [list(map(int, input().split())) for i in range(m)]
c, d = 0, 0
for i in range(len(a)):
    if i%2==0:
        c = c+sum(a[i])
    else:
        d = d+sum(a[i])
print(c, d)