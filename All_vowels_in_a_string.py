s = input()
a = ['a','e','i','o','u']
c = 0
for i in s:
    if i in a:
        c = c+1
        a.remove(i)
    else:
        continue
if c>=5:
    print(True)
else:
    print(False)