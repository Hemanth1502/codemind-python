n = int(input())
f=0
if n%2!=0:
    print(False)
else:
    i=0
    while(i!=n):
        if 2**i==n:
            f=1
            break
        else:
            i=i+1
    if f==1:
        print(True)
    else:
        print(False)