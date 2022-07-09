s1 = str(input()).lower()
s2 = str(input()).lower()
c = 0
for i in s1:
    if i in s2:
        c = c+1
    else:
        continue
if c==len(s1):
    print(True)
else:
    print(False)