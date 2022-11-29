s = list(str(input()))
a = []
for i in range(len(s)):
    if s[i].isalpha():
        a.append(s[i])
a=a[::-1]
c = 0
for i in range(len(s)):
    if s[i].isalpha():
        s[i]=a[c]
        c=c+1
print("".join(s))