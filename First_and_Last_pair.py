n = int(input())
a = list(map(int, input().split()))
k = len(a)
if k%2==0:
    k = k
else:
    k = k+1
    a.insert(k//2,0)
b = []
for i in range(k//2):
    b.append(a[i])
    b.append(a[-(1+i)])
print(*b)