a, b, k = map(int, input().split())
c = 0
for i in range (a, b+1):
    if i%k == 0:
        c = c+1
    else:
        continue
print(c)