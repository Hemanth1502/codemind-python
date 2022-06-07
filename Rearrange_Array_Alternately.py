n = int(input())
while(n):
    m = int(input())
    a = list(map(int, input().split()))
    k = len(a)
    if k%2==0:
        k = (k//2)-1
    else:
        k = (k//2)-1
    b = a[0:k+1]
    c = a[k+1:]
    d = c[::-1]
    e = []
    if len(b)==len(d):
        for i in range((len(a)//2)):
            e.append(d[i])
            e.append(b[i])
    elif len(b)<len(d):
        for i in range(len(b)):
            e.append(d[i])
            e.append(b[i])
        x = d[-1]
        e.append(x)
    elif len(b)>len(d):
        for i in range(len(d)):
            e.append(d[i])
            e.append(b[i])
        y = b[-1]
        e.append(y)
    else:
        continue
    print(*e)
    n-=1