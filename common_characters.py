s1 = list(str(input()).lower())
s2 = list(str(input()).lower())
a = []
for i in s1:
    if i in s2:
        a.append(i)
for i in a:
    if i == ' ':
        a.remove(i)
a = sorted(list(set(a)))
if len(a)>0:
    print(''.join(sorted(a)))
else:
    print(-1)