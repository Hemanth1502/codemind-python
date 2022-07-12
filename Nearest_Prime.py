def prime(n):
    for i in range(2,n):
        if n%i==0:
            return 0
    else:
        return 1
t = int(input())
for i in range(t):
    n = int(input())
    i = n+1
    while(True):
        if prime(i):
            p1 = i
            break
        else:
            i = i+1
    j = n
    while(True):
        if prime(j):
            p2 = j
            break
        else:
            j=j-1
    if abs(p1-n)>abs(p2-n):
        print(p2)
    elif abs(p1-n)==abs(p2-n):
        print(min(p1, p2))
    elif abs(p1-n)<abs(p2-n):
        print(p1)