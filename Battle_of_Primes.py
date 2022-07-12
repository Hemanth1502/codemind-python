def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1
a = int(input())
b = int(input())
i = a+b+1
while(True):
    if prime(i):
        print(i-(a+b))
        break
    else:
        i+=1