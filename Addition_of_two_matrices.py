n = int(input())
x =[list(map(int, input().split())) for i in range(n)]
y =[list(map(int, input().split())) for i in range(n)]
for i in range(n):
    c = []
    for j in range(n):
        c.append((int(x[i][j])+int(y[i][j])))
    print(*c)