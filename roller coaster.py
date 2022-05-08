t = int(input())
while t>0:
    x,h = map(int,input().split())
    if (x>=h):
        print("YES")
    else:
        print("NO")
    t-=1     
