n = int(input())
a = list(map(int, input().split()))
c = 0
for i in range(n):
    if i==0 or i%2==0:
        c = c + a[i]
    else:
        continue
print(c)