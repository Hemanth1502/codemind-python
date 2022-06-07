n = int(input())
a = list(map(int, input().split()))
b = int(input())
if b in a:
    print(a.index(b))
else:
    print(-1)