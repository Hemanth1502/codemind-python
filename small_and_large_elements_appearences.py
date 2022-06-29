s = list(input())
for i in s:
    if ' ' in s:
        s.remove(' ')
    else:
        continue
a = []
a.append(min(s))
a.append(s.count(min(s)))
a.append(max(s))
a.append(s.count(max(s)))
print(*a)