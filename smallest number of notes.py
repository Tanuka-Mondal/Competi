t = int(input())
money = [100,50,10,5,2,1]

while(t!=0):
    note=0
    p=int(input())
    for i in money:
        if(p>=i):
            note=note+(p//i)
            p=p%i 
    print(note)    
    t-=1 
