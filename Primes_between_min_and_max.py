def prime(n):
    for i in range(2,n):
        if n%i==0:
            return 0
    else:
        return 1
n = int(input())
a = list(map(int, input().split()))
p1 = a.index(min(a))
p2 = a.index(max(a))
if p1>p2:
    p1,p2=p2,p1
c = 0
for i in range(p1, p2+1):
    if prime(a[i]) and a[i]!=1:
        c = c+1
print(c)