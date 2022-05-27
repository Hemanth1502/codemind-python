n = input()
l = list(n)
c = 0
c1 = 0
c2 = 0
for i in range (0, len(l)):
    if int(l[i])%2 == 0:
        c = c+1
    elif int(l[i])%2 != 0:
        c1 = c1 + 1
    else:
        c2 = 0
if c == len(l):
    print('Even')
elif c1 == len(l):
    print('Odd')
else:
    print('Mixed')