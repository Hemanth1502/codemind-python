s = list(str(input()))
a = []
for i in range(len(s)):
    if int(s[i])%2!=0:
        a.append(str(int(s[i])**2))
print(''.join(a))