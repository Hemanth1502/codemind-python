def prime(n):
    for i in range (2,n):
        if n%i==0:
            return 0
    else:
        return 1
n = int(input())
a = []
for i in range (2,n+1):
    if prime(i):
        a.append(i)
    else:
        continue
f = 0
x = 0
y = 0
for i in range (0,len(a)):
    for j in range (0,len(a)):
        if a[i]*a[j]==n:
            f = f + 1
            x = a[i]
            y = a[j]
        else:
            continue
if f>=1:
    s = min(x, y)
    s1 = max(x, y)
    print(s, s1)
else:
    print(-1)