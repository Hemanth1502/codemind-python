n = int(input())
i=0
while(True):
    if abs(n-(2**i))==0:
        print(0)
        break
    elif n-(2**i)<0:
        c=(2**(i-1))
        d=(2**(i))
        print(min(abs(c-n),abs(d-n)))
        break
    i=i+1