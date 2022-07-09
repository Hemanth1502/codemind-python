s = (str(input()).lower()).split()
c = 0
for i in range(len(s)):
    if s[i]==s[i][::-1]:
        c = c+1
    else:
        continue
print(c)