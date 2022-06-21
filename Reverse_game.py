n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n):
    x = str(a[i])
    x = int(x[::-1])
    b.append(x)
print(*b)