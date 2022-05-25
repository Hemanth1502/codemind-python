n = int(input())
while(n):
    a, b = map(int, input().split())
    c = input()
    C = list(str(c))
    g = []
    for i in range (b-1, -1, -1):
        x = C[0:i+1]
        y = C[i+1:]
        xr = x[::-1]
        C = xr + y
        g = ''.join(C)
    print(g)