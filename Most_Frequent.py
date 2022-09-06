n = int(input())
a = list(map(int, input().split()))
maxx = []
for i in a:
    maxx.append(a.count(i))
k = max(maxx)
b = []
for i in a:
    if a.count(i)==k:
        b.append(i)
print(min(b))