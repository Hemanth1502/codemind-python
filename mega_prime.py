def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if(c==2):
        return 1
    else:
        return 0
n = int(input())
temp = n
if prime(n):
    c = 0
    a = list(str(n))
    s = len(a)
    for i in range(0,s):
        x = int(a[i])
        if prime(x):
            c = c + 1
        else:
            continue
    if c == s:
        print('Mega Prime')
    else:
        print('Not Mega Prime')
else:
    print('Not Mega Prime')