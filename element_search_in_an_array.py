n = int(input())
a = list(map(int, input().split()))
b = int(input())
f = 0
for i in range(n):
    if a[i]==b:
        f = 1
    else:
        continue
if f == 1:
    print(True)
else:
    print(False)