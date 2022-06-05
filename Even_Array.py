n = int(input())
a = list(map(int, input().split()))
c = 0
for i in range(len(a)):
    if a[i]==0 or a[i]%2==0:
        c = c+1
    else:
        continue
if c==len(a):
    print(True)
else:
    print(False)