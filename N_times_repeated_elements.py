n = int(input())
a = list(map(int, input().split()))
k = int(input())
s = []
for i in range(len(a)):
    if a.count(a[i])==k:
        s.append(a[i])
b = []
for i in s:
    if i not in b:
        b.append(i)
if len(b)>0:
    print(*(b))
else:
    print('-1')