a = list(map(int, input().split()))
k = max(a)
a.remove(k)
k1 = max(a)
print((k-1)*(k1-1))