n = int(input())
a = list(map(int, input().split()))
b = []
if n%2==0:
    for i in range(len(a)):
        b.append(a[i])
else:
    for i in range(len(a)):
        b.append(a[i])
    b.append(0)
print(*b)