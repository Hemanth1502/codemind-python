n = int(input())
a = list(map(int, input().split()))
for i in range(len(a)):
    if a[i]==0:
        temp = a[i]
        a.remove(temp)
        a.append(temp)
    else:
        continue
print(*a)