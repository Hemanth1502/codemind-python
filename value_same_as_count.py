n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n):
    if a[i]==a.count(a[i]):
        b.append(a[i])
print(len(set(b)))