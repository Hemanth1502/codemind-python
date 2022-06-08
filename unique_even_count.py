n = int(input())
a = list(map(int, input().split()))
b = []
for i in a:
    if i not in b:
        b.append(i)
    else:
        continue
c = 0
for i in range(len(b)):
    if b[i]%2==0:
        c = c+1
    else:
        continue
print(c)