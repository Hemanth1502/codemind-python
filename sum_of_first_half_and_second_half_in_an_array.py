n = int(input())
a = list(map(int, input().split()))
a1 = a[:n//2]
a2 = a[n//2:]
print(sum(a1))
print(sum(a2))