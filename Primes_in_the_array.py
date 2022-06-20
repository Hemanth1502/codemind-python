def prime(n):
    for i in range(2, n):
        if n%i==0:
            return 0
    else:
        return 1
n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n):
    if prime(a[i]) and a[i]!=1:
        b.append(a[i])
    else:
        continue
print(len(b))