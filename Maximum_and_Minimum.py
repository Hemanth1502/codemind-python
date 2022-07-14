n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n):
    if a[i]==a.count(a[i]):
        b.append(a[i])
if len(b)>0:
    print(min(b), max(b))
else:
    print('-1')