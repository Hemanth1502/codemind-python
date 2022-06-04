n = int(input())
a = list(map(int, input().split()))
b = (sum(a)//n)
f = 0
for i in range(n):
    if a[i]==b:
        f = 1
if f == 1:
    print('True')
else:
    print('False')