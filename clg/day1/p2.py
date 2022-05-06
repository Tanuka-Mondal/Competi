for i in range(int(input())):
    x = int(input())
    m = x%12
    if m == 1:
        print(x+11,'WS')
    elif m == 2:
        print(x+9,'MS') 
    elif m == 3:
        print(x+7,'AS')  
    elif m == 4:
        print(x+5,'AS') 
    elif m == 5:
        print(x+3,'MS')  
    elif m == 6:
        print(x+1,'WS')    
    elif m == 7:
        print(x-1,'WS') 
    elif m == 8:
        print(x-3,'MS')   
    elif m == 9:
        print(x-5,'AS')   
    elif m == 10:
        print(x-7,'AS')    
    elif m == 11:
        print(x-9,'MS')   
    elif m == 0:
        print(x-11,'WS')                              
