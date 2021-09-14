try:
    t = int(input())
    while(t!=0):
        a,b = map(int,input().split())
        sum = a+b
        print(sum)
        t-=1
except:
    pass
