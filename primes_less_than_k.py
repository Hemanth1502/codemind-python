def prime(n):
    for i in range(2,n):
        if n%i==0:
            return 0
    else:
        return 1
n = int(input())
a = list(map(int, input().split()))
k = int(input())
c = 0
for i in range(n):
    if prime(a[i]) and a[i]!=1 and a[i]<=k:
        c = c+1
    else:
        continue
print(c)