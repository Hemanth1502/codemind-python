n = int(input())
a = list(map(int, input().split()))
e = []
o = []
for i in range(len(a)):
    if a[i]%2==0:
        e.append(a[i])
    else:
        o.append(a[i])
print(*(e+o))