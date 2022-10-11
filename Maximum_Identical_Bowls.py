n = int(input())
a=list(map(int, input().split()))
b=sum(a)
if b%n==0:
    print(n)
else:
    while(True):
        if b%n==0:
            print(n)
            break
        else:
            n=n-1