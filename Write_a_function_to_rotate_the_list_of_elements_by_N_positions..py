n = int(input())
a = list(map(int, input().split()))
k = int(input())
if k>n:
    b = a[-k%n:]+a[:-k%n]
    print(*b)
else:
    print(*a[-k:]+a[:-k])