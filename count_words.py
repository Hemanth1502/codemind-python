def vowel(s):
    for i in s:
        if i in 'aeiouAEIOU':
            return 1
    else:
        return 0
s = input().split()
k = len(s)
c = 0 
for i in range(k):
    s1 = list(s[i])
    if vowel(s1[0]) and s1[len(s1)-1]!=vowel:
        c = c+1
    else:
        continue
print(c)