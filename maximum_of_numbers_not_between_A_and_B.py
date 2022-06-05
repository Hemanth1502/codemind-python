n = int(input())
a = list(map(int, input().split()))
b = []
x, y = map(int, input().split())
for i in range (len(a)):
    if a[i]>=x and a[i]<=y:
        continue
    else:
        b.append(a[i])
if len(b)>0:
    print(max(b))
else:
    print(-1)