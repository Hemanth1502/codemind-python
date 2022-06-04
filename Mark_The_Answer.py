m, n = map(int, input().split())
a = list(map(int, input().split()))
c = 0
d = 0
for i in range(len(a)):
    if a[i]<=n:
        c+=1
    else:
        if a[i]>n:
            d+=1
            if d == 2:
                break
            else:
                continue
        else:
            continue
print(c)