n = int(input())
a = list(map(int, input().split()))
c = 0
for i in range(2,n-1):
    if a[i]==a[i-1]+a[i-2]:
        c = c+1
    else:
        continue
if c==len(a)-3:
    print('yes')
else:
    print('no')