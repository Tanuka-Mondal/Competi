t = int(input())

while(t!=0):
    n = input()
    if(n=='b' or n=='B'):
        print('BattleShip')
    elif(n=='c' or n=='C'):
        print('Cruiser')  
    elif(n=='d' or n=='D'):
        print('Destroyer') 
    elif(n=='f' or n=='F'):
        print('Frigate')      
    t-=1 
