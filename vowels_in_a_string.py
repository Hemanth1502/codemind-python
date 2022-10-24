s = str(input())
k = input()
v = 'aeiouAEIOU'
if k in s:
    print(True)
    print(s.index(k))
else:
    print(False)