a = int(input())
n = list(str(a))
c = 0
for i in range(len(n)):
    n[i]=int(n[i])
for i in range(len(n)):
    c = c+(n[i]**(i+1))
if a==c:
    print('True')
else:
    print('False')