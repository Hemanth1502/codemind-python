a, b = map(int, input().split())
i = 2
while(True):
    if i%a==0 and i%b==0:
        print(i)
        break
    else:
        i = i+1