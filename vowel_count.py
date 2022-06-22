s = input()
v = ['a','e','i','o','u','A','E','I','O','U']
c = 0
for i in s:
    if i in v:
        c = c+1
    else:
        continue
print(c)