a = input()
b = str(a)
h = b[0:2]
c = b[2]
m = b[3:5]
hi = int(h)
mi = int(m)
if(hi>12):
    hi = hi-12
ha = 0.5*(hi*60 + mi)
ma = 6*mi
angle = abs(ha - ma)
if(angle>180):
    angle = abs(angle-360)
print(angle)