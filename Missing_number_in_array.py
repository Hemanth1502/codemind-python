n = int(input())
while(n):
    m = int(input())
    x = list(map(int, input().split()))
    a = []
    c = 0
    for i in range (m):
        c = c+1
        a.append(c)
    b = []
    for j in a:
        if j not in x:
            b.append(j)
        else:
            continue
    print(*b)
    n-=1