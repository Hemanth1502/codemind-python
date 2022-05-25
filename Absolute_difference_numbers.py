N, X = map(int, input().split())
n = list(str(N))
A = []
z = n[0:X]
A = ''.join(z)
Z = int(A)
a = []
c = n[-1:-X-1:-1]
a = ''.join(c)
b = int(a)
r = 0
while(b):
    d = b%10
    r = r*10 + d
    b = b//10
y = abs(Z-r)
print(y)