t = int(input())
while(t!=0):
    n = int(input())
    if (n<6):
        print(0)
    elif (n>=6):
        print((n+1)//7)
    t-=1    
