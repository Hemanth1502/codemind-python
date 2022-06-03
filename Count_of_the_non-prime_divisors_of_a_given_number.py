def prime(n):
    c=0
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
           return 0
    return 1
n = int(input())
c = 0
d = 0
for i in range (1,n+1):
    if (n%i==0 and prime(i) and i!=1):
        c = c + 1
    if n%i==0:
        d = d + 1
print(abs(c-d))