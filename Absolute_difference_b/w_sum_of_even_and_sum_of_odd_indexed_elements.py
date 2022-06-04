n = int(input())
a = list(map(int, input().split()))
c = 0
d = 0
for i in range(n):
    if i==0 or i%2==0:
        c = c + a[i]
    else:
        if i%2!=0:
            d = d+a[i]
        else:
            continue
res = abs(c-d)
print(res)