n = int(input())
a = list(map(int, input().split()))
c = 0
for i in range(1,n):
    if a[i-1]<a[i]:
        c = c+1
    else:
        continue
if c+1==len(a):
    print('yes')
else:
    print('no')