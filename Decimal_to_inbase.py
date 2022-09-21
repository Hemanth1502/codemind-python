n = int(input())
t = int(input())
a = []
while(True):
    a.append(n%t)
    n=n//t
    if n<t:
        a.append(n)
        break
a=a[::-1]
count=0
b=[]
for i in range(len(a)):
    if a[i]==0:
        count=count+1
    else:
        count=0
    b.append(count)
if max(b)==0:
    print(-1)
else:
    print(max(b))