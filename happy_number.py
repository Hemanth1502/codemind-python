n = int(input())
temp = n
while(True):
    s = 0
    while(temp):
        d = temp%10
        s = s+d**2
        temp = temp//10
    if s<10:
        if s ==1 or s == 7:
            print(True)
            break
        else:
            print(False)
            break
    else:
        temp=s