n = int(input())
temp = n
a = 0
b = 1
f = 0
while(n):
    c = a + b
    a = b
    b = c
    if temp == c:
        f = 1
        break
    n-=1
if f == 1:
    print('True')
else:
    print('False')