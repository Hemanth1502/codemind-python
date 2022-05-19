n = int(input())
a = str(n)
b = list(a)
c = len(b)
d = set(a)
e = len(d)
if(c==e):
    print('Unique Number')
else:
    print("Not Unique Number")