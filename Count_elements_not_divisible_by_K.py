n, k = map(int, input().split())
a = list(map(int, input().split()))
c = 0
for i in range(len(a)):
    if a[i]%k!=0:
        c = c+1
print(c)