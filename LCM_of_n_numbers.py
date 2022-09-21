n = int(input())
a = list(map(int, input().split()))
i = 1
b=[]
while(True):
    count=0
    for j in range(len(a)):
        if i%a[j]==0:
            count=count+1
    if count==len(a):
        print(i)
        break
    i=i+1