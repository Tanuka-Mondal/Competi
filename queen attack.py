t = int(input())
while(t>0):
    n,x,y = map(int,input().split())
    s = 2*(n-1)
    s1 = min(x-1,y-1) 
    s2 = min(x-1,n-y)
    s3 = min(n-x,y-1)
    s4 = min(n-x,n-y)
    print(s+s1+s2+s3+s4)
    t-=1
