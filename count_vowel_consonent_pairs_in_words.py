s = (str(input()).lower()).split()
c = []
for i in range(len(s)):
    x = list(s[i])
    for i in range(len(x)//2):
        if x[i] in 'aeiou' and x[len(x)-(i+1)] not in 'aeiou':
            c.append((x[i],x[len(x)-(i+1)]))
        elif x[i] not in 'aeiou' and x[len(x)-(i+1)] in 'aeiou':
            c.append((x[i],x[len(x)-(i+1)]))
        else:
            continue
print(len(c))