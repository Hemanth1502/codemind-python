def prime(n):
    for i in range(2, int(n**0.5)+1):
        if(n%i==0):
            return 0
    return 1
n = int(input())
a = list(map(int, input().split()))
c = 0
d = 0
for i in range(n):
    if prime(a[i]) and a[i]!=1:
        d = d+1
        c = c+a[i]
    else:
        continue
print('%0.2f'%(c/d))