s1 = (str(input()).lower()).split()
s2 = (str(input()).lower()).split()
c = []
for i in s1:
    if i in s2:
        c.append(i)
    else:
        continue
print(len(c))