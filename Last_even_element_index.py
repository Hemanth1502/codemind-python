n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if a[i]%2==0:
        c = i
    else:
        continue
print(c)