n = int(input())
a = list(map(int, input().split()))
k = int(input())
p = a.index(k)
c = 0
for i in range(0, p+1):
    c = c+a[i]
print(c)