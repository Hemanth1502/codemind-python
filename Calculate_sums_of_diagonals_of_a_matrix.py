n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
b = []
for i in range(len(a)):
    c = []
    for j in range(len(a)):
        if i==j:
            c.append(a[i][j])
    b.append(sum(c))
d = sum(b)
g=[]
e = a[::-1]
for i in range(len(e)):
    f = []
    for j in range(len(e)):
        if i==j:
            f.append(e[i][j])
    g.append(sum(f))
h = sum(g)
print('Principal Diagonal:%d'%d)
print('Secondary Diagonal:%d'%h)