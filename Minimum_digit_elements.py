n = int(input())
a = list(map(int, input().split()))
c = 0
b = []
for i in range(len(a)):
    x = list(str(a[i]))
    b.append(len(x))
for i in range(len(a)):
    x = list(str(a[i]))
    if len(x)==min(b):
        c = c+1
print(c)