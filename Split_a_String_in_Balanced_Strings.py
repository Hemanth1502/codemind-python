s = list(str(input()))
c=0
b = []
a=[]
for i in range(len(s)):
    if s[i]=='R':
        c=c+1
        a.append('R')
    elif s[i]=='L':
        c=c-1
        a.append('L')
    if c==0:
        b.append("".join(a))
        a=[]
print(len(b))