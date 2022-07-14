n = int(input())
a = list(map(int, input().split()))
a1 = a[0:(n//2)]
a2 = a[(n//2):]
print(abs(sum(a1)-sum(a2)))