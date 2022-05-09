t = int(input())
while(t>0):
    x,y = map(int,input().split())
    if(x>y):
        print("A")
    else:
        print("B")
    t-=1   
