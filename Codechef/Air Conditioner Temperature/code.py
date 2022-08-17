# cook your dish here
t = int(input())
while(t > 0):
    a,b,c = map(int,input().split())
    if b >= a and b >= c :
        print("Yes")
    else :
        print("No")
    t -= 1    
