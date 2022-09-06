t = int(input())
for i in range(t):
    n,r = map(int,input().split())
    a = list(map(int, input().split()))
    for i in range(r):
        a = [a[-1]]+a[0:n-1]
    print(*a)