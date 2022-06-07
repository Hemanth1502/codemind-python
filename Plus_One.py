n = int(input())
a = list(map(str, input().split()))
b = ''.join(a)
c = int(b)
d = c+1
print(*list(str(d)))