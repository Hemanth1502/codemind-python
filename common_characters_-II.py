s1 = str(input()).lower()
s2 = str(input()).lower()
a = list(set(s1)&set(s2))
for i in a:
    if ' ' in a:
        a.remove(' ')
    else:
        continue
print(len(a))