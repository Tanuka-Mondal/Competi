t = int(input())
c=0
d=0
while(t!=0):
    a,b=map(int,input().split())
    if(a>b):
        c=a 
    else:
        c=b 
    d = a+b 
    print(c,d)
    t-=1 
    
