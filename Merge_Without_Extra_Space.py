n = int(input())
while(n):
    x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = a+b
    print(*sorted(c))
    n-=1