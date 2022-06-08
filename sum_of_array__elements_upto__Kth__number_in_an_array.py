n = int(input())
a = list(map(int, input().split()))
k = int(input())
ki = a.index(k)
c = 0
for i in range(0,ki+1):
    c = c + a[i]
print (c)