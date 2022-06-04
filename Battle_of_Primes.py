def prime(n):
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
           return 0
    return 1
a = int(input())
b = int(input())
i = 1
while(True):
    c = a+b+i
    if prime(c):
        print(i)
        break
    i = i+1