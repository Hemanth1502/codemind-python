def prime(n):
    c=0
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
           return 0
    return 1
a = int(input())
b = int(input())
c = []
for i in range (a, b+1):
    if (prime(i) and i!=1):
        c.append(i)
    else:
        continue
print(len(c))