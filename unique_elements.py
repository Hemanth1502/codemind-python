n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])
    else:
        continue
print(*b)