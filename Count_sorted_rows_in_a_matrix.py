n, m = map(int, input().split())
c = 0
for i in range(n):
    a = list(map(int, input().split()))
    if a==sorted(a):
        c = c+1
    elif a == sorted(a)[::-1]:
        c = c+1
print(c)