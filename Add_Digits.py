n = int(input())
while(n):
    n = str(n)
    l = len(n)
    if l==1:
        print(int(n))
        break
    else:
        n = list(str(n))
        for i in range(len(n)):
            n[i]=int(n[i])
        s = sum(n)
        n = s