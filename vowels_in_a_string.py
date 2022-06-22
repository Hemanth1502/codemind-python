s = input()
k = input()
v = ['a','e','i','o','u','A','E','I','O','U']
if k in s:
    print(True)
    print(s.index(k))
else:
    print(False)