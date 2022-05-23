n = int(input())
k = n**2
s1 = str(n)
l1 = len(s1)
s2 = str(k)
l2 = len(s2)
if(s1==s2[l1:]):
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')