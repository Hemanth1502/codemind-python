k = int(input())
k1 = int(str(k)[::-1])
if (k**2)==int(str(k1**2)[::-1]):
    print('True')
else:
    print('False')