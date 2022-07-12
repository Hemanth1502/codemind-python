n = int(input())
a = []
for i in range(1,n):
    if n%i==0:
        a.append(i)
if sum(a)==n:
    print('True')
else:
    print('False')