n = int(input())
a = list(map(int, input().split()))
k = sum(a)//n
c = 0
for i in range(len(a)):
    if a[i]<=k:
        c = c+1
    else:
        continue
print(c)