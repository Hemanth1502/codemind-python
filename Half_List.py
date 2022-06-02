n = int(input())
a = list(map(int, input().split()))
if n % 2==0:
    k=n//2
else:
    k = (n//2)+1
b = a[:k:]
c = a[:k-1:-1]
print(*(c+b))