s = list(str(input()))
a=[]
for i in s:
    if i in 'aeiouAEIOU':
        a.append(i)
if len(a)>0:
    b=[]
    for i in a:
        if i not in b:
            b.append(i)
    print(*b)
else:
    print(-1)