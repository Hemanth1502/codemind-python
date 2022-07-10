m, n = map(int, input().split())
x = []
for i in range(m):
    a = list(map(int, input().split()))
    x.append(a)
b = []
for i in range(n):
    c = []
    for j in range(m):
        c.append(x[j][i])
    b.append(c)
# y = []
# for i in range(len(b)):
#     y.append(sum(b[i]))
# print(sum(y))
count = 0
for i in range(len(b)):
    if b[i]==sorted(b[i]):
        count = count+1
    elif b[i]==sorted(b[i])[::-1]:
        count=count+1
print(count)