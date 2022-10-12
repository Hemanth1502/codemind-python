t=int(input())
for i in range(t):
    n=int(input())
    b=1
    for i in range(2,n+1):
        if i%2==0:
            b=b^i
        else:
            b=b&i
    print(b)