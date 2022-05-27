L = int(input())
N = int(input())
while(N):
    W, H = map(int, input().split())
    if W<L or H<L:
        print('UPLOAD ANOTHER')
    else:
        if (W>=L and H >= L) and W == H:
            print('ACCEPTED')
        else:
            print('CROP IT')
    N-=1