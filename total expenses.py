t=int(input())
while(t!=0):
    total=0
    q,p=map(float,input().split())
    total = q*p 
    if(q>1000):
        total = total - (total/10)
    print(total)    
    t-=1
    
