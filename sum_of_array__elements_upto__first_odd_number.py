n = int(input())
a = list(map(int, input().split()))
c = 0
for i in range(n):
    if a[i]%2!=0:
        break
    else:
        c = c+a[i]
print(c)