s1 = (str(input()).lower()).split()
s2 = (str(input()).lower()).split()
a = []
b = []
for i in s1:
    if s1.count(i)==1:
        a.append(i)
    else:
        continue
for i in s2:
    if s2.count(i)==1:
        b.append(i)
    else:
        continue
c = []
for i in a:
    if i in b:
        c.append(i)
    else:
        continue
print(len(c))