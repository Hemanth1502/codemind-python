s = list(str(input()).lower())
for i in s:
    if ' ' in s:
        s.remove(' ')
    else:
        continue
a = []
for i in s:
    if i not in a:
        a.append(i)
    else:
        continue
g = ''.join(sorted(a))
print(g)