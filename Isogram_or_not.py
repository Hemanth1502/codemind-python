s = str(input()).lower()
s = list(s)
c = 0
for i in range(len(s)):
    if s.count(s[i])==1:
        c = c+1
    else:
        continue
if len(s)==c:
    print(True)
else:
    print(False)