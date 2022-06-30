s1 = input().split()
for i in range(len(s1)):
    s1[i]=str(s1[i]).lower()
s2 = input().split()
for i in range(len(s2)):
    s2[i]=str(s2[i]).lower()
a = []
for i in s2:
    if i in s1:
        a.append(i)
    else:
        continue
print(*a)