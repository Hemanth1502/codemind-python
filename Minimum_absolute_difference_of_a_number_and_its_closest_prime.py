def prime(n):
    for i in range (2,n):
        if n%i==0:
            return 0
    else:
        return 1
n = int(input())
for i in range (2,n+1):
    if prime(i):
        c = i
i = n+1
while(1):
    if prime(i):
        d = i
        break
    i+=1
if abs(n-c)==abs(n-d):
    s = min(c,d)
elif abs(n-c)>abs(n-d):
    s = d
elif abs(n-c)<abs(n-d):
    s = c
else:
    s = n
print(abs(s-n))