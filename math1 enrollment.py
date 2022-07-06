t = int(input())
while(t>0):
    x,y = map(int,input().split())
    if (x>=y):
        print(0)
    else:  
        print(y-x)
    t-=1    
