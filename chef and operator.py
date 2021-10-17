t = int(input())
while (t!=0):
    a,b = map(int,input().split())
    if (a<b):
        print('<')
    elif (a>b):
        print('>')
    elif(a == b):
        print('=')
    t-=1 
