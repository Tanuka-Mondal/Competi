def sumf(x):
    mySum = 0
    for i in range(x+1):
        mySum=mySum+i
    return mySum
    
t = int(input())
while(t!=0):
    d,n = map(int,input().split())
    ans = n
    while(d!=0):
        ans = sumf(ans)
        d-=1 
    print(ans)    
    t-=1     
