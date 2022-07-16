s = list(str(input()).lower())
for i in s:
    if i==' ':
        s.remove(i)
a = []
for i in s:
    if s.count(i)==1:
        a.append(i)
if len(a)>0:
    print(a[0])
else:
    print(-1)