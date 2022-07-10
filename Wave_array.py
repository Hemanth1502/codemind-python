n = int(input())
# print(n)
a = list(map(int, input().split()))
c = 0
for i in range(n-1):
    if a[i]>a[i-1] and a[i]>a[i+1]:
        c = c+1
    elif a[i]<a[i-1] and a[i]<a[i+1]:
        c = c+1
# print(c)
if c+1==n:
    print('yes')
else:
    print('no')