t=int(input())
for i in range(t):
    n=int(input())
    a=list(bin(n)[2:])
    count=0
    for i in range(len(a)):
        if a[i]=='1':
            count=count+1
    print(count)