n = input().split()
x = list(n)
a = []
for i in range(len(x)):
    x1 = list(x[i])
    x2 = len(x1)
    a.append(x2)
print(*a)