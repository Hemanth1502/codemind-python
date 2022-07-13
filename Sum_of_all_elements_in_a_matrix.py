m, n = map(int, input().split())
a = [list(map(int, input().split())) for i in range(m)]
b = []
for i in range(len(a)):
    b.append(sum(a[i]))
print(sum(b))