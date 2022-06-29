s = input().split()
a = []
s1 = list(s[0])
s2 = list(s[-1])
a.append(min(s1))
a.append(max(s2))
print(*a)