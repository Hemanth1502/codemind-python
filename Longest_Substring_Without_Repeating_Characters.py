s = list(str(input()))
l=[]
maxx=-1
for i in range(len(s)):
    for j in range(i):
        if len(list(str("".join(s[j:i]))))==len(list(set(list(str("".join(s[j:i])).lower())))) and len(s[j:i])>maxx:
            l.append("".join(s[j:i]))
            maxx = len(s[j:i])
if len(l[-1])>=3:
    print(l[-1])
else:
    print(-1)