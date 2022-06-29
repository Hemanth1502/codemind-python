s = input().split()
for i in range(len(s)-1):
    if len(s[i])<len(s[i+1]):
        continue
    elif len(s[i])==len(s[i+1]):
        a = min(s[i], s[i+1])
        b = max(s[i], s[i+1])
        s[i]=a
        s[i+1]=b
    elif len(s[i])>len(s[i+1]):
        temp = s[i]
        s[i] = s[i+1]
        s[i+1] = temp
print(*s)
# print(*sorted(input().split()))