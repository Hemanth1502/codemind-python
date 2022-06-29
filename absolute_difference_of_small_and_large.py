s = input().split()
for i in range(len(s)):
    print(abs((ord(min(s[i])))-(ord(max(s[i])))), end=' ')