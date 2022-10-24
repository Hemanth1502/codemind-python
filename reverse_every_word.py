s = str(input()).split()
for i in range(len(s)):
    s[i]=s[i][::-1]
print(*s)