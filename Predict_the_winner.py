n = int(input())
a = list(map(int, input().split()))
x = []
y = []
for i in range(len(a)):
    if i%2!=0:
        x.append(a[i])
    else:
        y.append(a[i])
sx = sum(x)
sy = sum(y)
if (sx-sy)%4==0:
    print('X')
else:
    print('Y')