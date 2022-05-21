a, b = map(int, input().split())
k = max(a,b)
c = a-b
if(c==-1 or c==1):
    print("Yes")
elif(k==10 and c==9 or c==-9):
    print('Yes')
else:
    print("No")