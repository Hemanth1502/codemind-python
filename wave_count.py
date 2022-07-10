n = int(input())
a = list(map(int, input().split()))
c = 0
for i in range(n-1):
    if a[i]>a[i-1] and a[i]>a[i+1]:
        c = c+1
    elif a[i]<a[i-1] and a[i]<a[i+1]:
        c = c+1
if c+1==n:
    print(c//2)
else:
    print(-1)