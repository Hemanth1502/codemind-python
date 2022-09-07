n = input()
n = list(n)
for i in n:
    if i.isdigit():
        continue
    else:
        n.remove(i)
for i in range(len(n)):
    n[i]=int(n[i])
y = []
for i in range(len(n)):
    x = []
    for j in range(1,n[i]+1):
        if n[i]%j==0:
            x.append(j)
    y.append(sum(x))
dic={}
for i in range (len(n)):
    dic[n[i]]=y[i]
z = []
for i in dic:
    if dic[i] in n:
        z.append(i)
if len(z)>0:
    print(*z)
else:
    print(-1)