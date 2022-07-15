n = int(input())
a = list(map(int, input().split()))
x, y = map(int, input().split())
s = []
for i in range(len(a)):
    if a[i]>=x and a[i]<=y:
        continue
    else:
        s.append(a[i])
print(sum(set(s)))