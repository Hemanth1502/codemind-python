t = int(input())
for i in range(t):
    a = list(str(input()))
    c=0
    for i in range(len(a)):
        a[i]=int(a[i])
    a = sorted(a)
    for i in range(len(a)-1):
        if a[i+1]==a[i]+1:
            c = c+1
    if c+1==len(a):
        print('YES')
    else:
        print('NO')