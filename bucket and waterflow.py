t = int(input())
while(t>0):
    w,x,y,z = map(int,input().split()) 
    if ((x-w)>(y*z)):
        print("Unfilled")
    elif ((x-w)==(y*z)):
        print("filled")    
    elif ((x-w)<(y*z)):
        print("overflow")
    t -= 1
