n = int(input())
p = []
h = []
for i in range(n):
    p.append(int(input()))
for i in range(n):
    h.append(int(input()))
c=len(h)
i=0
j=0
a=[]
while(True):
    if p[i]<=h[j] and j not in a:
        a.append(j)
        i=i+1
        j=0
        c=c-1
    else:
        j=j+1
    if j == len(p):
        i=i+1
        j=0
    if i==len(p):
        break
print(c)