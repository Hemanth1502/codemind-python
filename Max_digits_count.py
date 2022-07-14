n = int(input())
a = list(map(int, input().split()))
b = []
c = 0
for i in range(len(a)):
    x = list(str(a[i]))
    b.append(len(x))
for i in range(len(a)):
    x = list(str(a[i]))
    if len(x)==max(b):
        c=c+1
print(c)