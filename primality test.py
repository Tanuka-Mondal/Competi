t = int(input())

while(t!=0):
    count=0
    n=int(input())
    if n==1:
        print('no')
    else:    
        for i in range(2,n//2):
            if(n%i == 0):
                count+=1
        if(count>=1):
            print('no')
        else:
            print('yes')
    t-=1 
