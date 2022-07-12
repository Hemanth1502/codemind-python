n = int(input())
temp = n
sn = int(n**2)
s = 0
while(sn):
    d = sn%10
    s = s+ d
    sn = sn//10
if s == temp:
    print('Neon Number')
else:
    print('Not Neon Number')