m = int(input())
n = int(input())
c = 0
while(m):
    x = list(map(int, input().split()))
    c = c+sum(x)
    m-=1
print(c)