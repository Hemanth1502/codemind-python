n = int(input())
a = list(map(int, input().split()))
k = int(input())
x = []
for i in range(len(a)):
    if a[i]==k:
        x.append(i)
    else:
        continue
if len(x)>0:
    print(min(x), max(x))
else:
    print(*[-1, -1])