n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    c = 0
    if a[i]%2==1:
        c = c + a[i]
    else:
        continue
print(i)