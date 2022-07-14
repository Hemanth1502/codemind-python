n = int(input())
a = list(map(int, input().split()))
if n%2!=0:
    k=n//2 + 1
    a.insert(k,0)
else:
    k = n//2
b = []
for i in range(k):
    b.append(a[i])
    b.append(a[len(a)-(i+1)])
print(*b)