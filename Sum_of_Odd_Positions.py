n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n):
    if i%2!=0:
        b.append(a[i])
    else:
        continue
print(sum(b))