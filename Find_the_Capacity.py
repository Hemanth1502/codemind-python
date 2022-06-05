# d ---- 2s
# 1s ----- t tr
# 1t ------ s sec
# 1s ----- b bl
# 1b ---- 512
# t, s, 
# 2 15 20 30 
a, b, c = map(int, input().split())
d = 2*a*b*c*512
e = int(d/1024)
f = str(e)
g = 'KB'
h = f+g
print(h)