t = int(input())
while t>0:
    x,y = map(int,input().split())
    r = (x*107)/100
    if (y<=r):
        print("YES")
    else:
        print("NO")
    t-=1    
