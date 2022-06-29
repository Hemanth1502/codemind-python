s = input().split()
a = []
for i in range(len(s)):
    s1 = list(s[i])
    a.append(min(s1))
    a.append(max(s1))
print(*a)