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
for i in range(len(a)):
    if prime(a[i]) and a[i]<=k and a[i]!=1:
        c=c+1
print(c)