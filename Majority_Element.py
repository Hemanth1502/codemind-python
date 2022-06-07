n = int(input())
a = list(map(int, input().split()))
k = n//2
for i in range(len(a)):
    if a.count(a[i])>k:
        print(a[i])
        break
    else:
        continue