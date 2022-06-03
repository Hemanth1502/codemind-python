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
if prime(n):
    temp = n
    c = 0
    dc = 0
    while(n):
        d = n%10
        n = n//10
        dc = dc + 1
        if prime(d):
            c = c + 1
    if c == dc:
        print('Mega Prime')
    else:
        print('Not Mega Prime')
else:
    print('Not Mega Prime')