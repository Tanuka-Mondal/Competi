for _ in range(int(input())):
    x,y,z = map(int,input().split())
    if((x+y)<=z):
        print(2)
    else:
        if(x<=z):
            print(1)
        else:
            print(0)
