s1 = list(str(input().lower()))
s2 = list(str(input().lower()))
s1 = list(set(s1))
s2 = list(set(s2))
a = []
for i in s1:
    if ' ' in s1:
        s1.remove(' ')
    else:
        continue
for i in s2:
    if ' ' in s2:
        s2.remove(' ')
    else:
        continue
for i in s1:
    if i not in s2:
        a.append(i)
    else:
        continue
for i in s2:
    if i not in s1:
        a.append(i)
    else:
        continue
a = ''.join(sorted(a))
print(a)