t = int(input())
while t>0:
    x,y,z = map(int,input().split())
    print((z-y)//x)
    t-=1     
