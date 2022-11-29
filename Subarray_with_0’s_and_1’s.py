n = int(input())
a = list(map(int, input().split()))
l=[]
maxx=-1
c = 0
d = 0
for i in range(len(a)):
    for j in range(i):
        if a[j:i].count(0)==a[j:i].count(1) and len(a[j:i])>=maxx:
            maxx=len(a[j:i])
            c = i-1
            d = j
if c==0 and d==0:
    print(-1)
else:
    print(d, c)