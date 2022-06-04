n = int(input())
a = list(map(int, input().split()))
d = 0
for i in range(n):
    if a[i]%2!=0:
        d = d+a[i]
    else:
        continue
print(d)