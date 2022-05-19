n = int(input())
arr = list(map(int, input().split()))
s1 = 0
s2 = 0
for i in range(0,n):
    if(i%2 == 0):
        s1 = s1+arr[i]
    else:
        s2 = s2+arr[i]
if (s2-s1 == 0):
    print('YES')
else:
    print('NO')