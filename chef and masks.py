t = int(input())
while t>0:
    x,y = map(int,input().split())
    if ((x*100)>=(y*10)):
        print("CLOTH")
    else:
        print("DISPOSABLE")
    t-=1     
