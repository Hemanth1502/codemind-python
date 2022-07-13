n = int(input())
k = int(n**2)
n = str(n)
k = str(k)
k1 = k[len(n):]
if int(n)==int(k1):
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')