n = int(input())
a = list(map(int, input().split()))
c = 0
for i in range(len(a)):
    if a[i]!=0 and a[i]!=1:
        print('False')
        break
else:
    print(True)