s = list(str(input()))
# print(s)
a = []
b = []
for i in range(len(s)):
    if s[i] in '!@#$%^&*()_-+={[}]|:;<>,.?/' or s[i]==' ':
        a.append(s[i])
    else:
        a.append('0')
for i in range(len(s)):
    if s[i] in '!@#$%^&*()_-+={[}]|:;<>,.?/' or s[i]==' ':
        b.append('0')
    else:
        b.append(s[i])
c = []
for i in b:
    if i=='0':
        b.remove(i)
b = ''.join(b).split()
for i in range(len(b)):
    b[i]=''.join(sorted(list(b[i])))
b = list(''.join(b))
while('0' in b):
    for i in b:
        if i=='0':
            b.remove(i)
j= 0
for i in range(len(a)):
    if a[i]=='0':
        a[i]=b[j]
        j = j+1
    else:
        continue
a = ''.join(a)
print(a)