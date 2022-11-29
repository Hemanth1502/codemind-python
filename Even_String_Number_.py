s = str(input())
a = []
c=0
for i in range(len(s)):
    if s[i].isdigit():
        a.append(s[i])
        if int(s[i])%2==0:
            c=c+1
if c==0:
    print(-1)
else:
    a=sorted(list(set(a)))
    b=[]
    d=[]
    co=0
    for i in range(len(a)):
        if int(a[i])%2==0 and co==0:
            b.append(a[i])
            co=co+1
        elif int(a[i])%2!=0 or co>0:
            d.append(a[i])
    a = []
    a=d[::-1]+b
    a=a
    print("".join(a))