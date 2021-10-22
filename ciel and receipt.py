t = int(input())
menu = []
for i in range(1,13):
    menu.append(2**(i-1))
menu.reverse()   
while(t!=0):
    item=0
    p=int(input())
    for i in menu:
        if(p>=i):
            item=item+(p//i)
            p=p%i 
    print(item)
    t-=1
