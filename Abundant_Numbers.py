n = int(input())
s = []
for i in range(1,n):
    if n%i==0:
        s.append(i)
if sum(s)>n:
    print('True')
else:
    print('False')