s = list(str(input()))
a = []
n = []
word=[]
num=[]
for i in range(len(s)):
    if s[i].isalpha():
        word.append(s[i])
    elif s[i].isdigit():
        num.append(s[i])
    elif s[i]==',':
        a.append(''.join(word))
        n.append(''.join(num))
        word=[]
        num=[]
    else:
        continue
a.append(''.join(word))
n.append("".join(num))
pas=[]
for j in range(len(a)):
    c = list(str(n[j]))
    for i in range(len(c)):
        c[i]=int(c[i])
    maxx=-1
    for z in range(len(c)):
        if c[z]>maxx and c[z]<=len(a[j]):
            maxx=c[z]
        else:
            continue
    if maxx==-1:
        pas.append('X')
    else:
        pas.append(a[j][maxx-1])
print(''.join(pas))