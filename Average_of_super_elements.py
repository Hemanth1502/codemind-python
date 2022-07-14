n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(len(a)):
    if a[i]==a.count(a[i]):
        b.append(a[i])
if len(b)>0:
    print('%0.2f'%(sum(set(b))/len(set(b))))
else:
    print(-1)