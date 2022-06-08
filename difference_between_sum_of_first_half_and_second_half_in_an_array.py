n = int(input())
a = list(map(int, input().split()))
if n%2==0:
    k = n//2
else:
    k = n//2
if len(a)%2==0:
    b = a[0:k]
    c = a[k:]
    s1 = sum(b)
    s2 = sum(c)
    print(abs(s1-s2))
else:
    b = a[0:k]
    c = a[k:]
    s1 = sum(b)
    s2 = sum(c)
    print(abs(s1-s2))