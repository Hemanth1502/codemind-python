n = int(input())
a = list(map(int, input().split()))
d = []
for i in range(len(a)):
    c = 1
    for j in range(len(a)):
        if i == j:
            continue
        else:
            c = c*a[j]
    d.append(c)
print(*d)