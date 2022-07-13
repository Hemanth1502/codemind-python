n = int(input())
f = 0
for i in range(n):
    if i*(i+1)==n:
        print('YES')
        f = 1
if f==0:
    print('NO')