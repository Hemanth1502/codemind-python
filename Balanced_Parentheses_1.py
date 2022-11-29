s = list(str(input()))
cc = 0
cf = 0
cs = 0
for i in range(len(s)):
    if s[i]=='(':
        cc=cc+1
    elif s[i]==')':
        cc=cc-1
    elif s[i]=="[":
        cf=cf+1
    elif s[i]=="]":
        cf=cf-1
    elif s[i]=="{":
        cs=cs+1
    elif s[i]=="}":
        cs=cs-1
if cc==0 and cf == 0 and cs == 0:
    print(True)
else:
    print(False)