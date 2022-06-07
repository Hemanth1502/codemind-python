n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    k = a.count(a[i])
    if k>1:
        print(a[i])
        break
    else:
        continue