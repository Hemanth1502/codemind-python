n = int(input())
a = list(map(int, input().split()))
i = 1
b=[]
while(True):
    count=0
    for j in range(len(a)):
        if a[j]%i==0:
            count=count+1
    if i>min(a):
        break
    if count==len(a):
        b.append(i)
    i=i+1
print(max(b))