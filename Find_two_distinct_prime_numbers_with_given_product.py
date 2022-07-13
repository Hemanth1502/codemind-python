def prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1
n = int(input())
a = []
for i in range(2,n):
    if n%i==0:
        if prime(i):
            a.append(i)
if len(a)>1:
    print(*a)
else:
    print(-1)