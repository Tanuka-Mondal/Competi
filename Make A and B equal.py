t = int(input())
while(t>0):
    a,b = map(int,input().split())
    if a == b :
        print("Yes")
    elif a > b:
        while(a>b):
            if b*2 == a :
                print("Yes")
            b *= 2
            if b > a:
                print("No")
    else:
        while(a<b):
            if a*2 == b :
                print("Yes")
            a *= 2
            if b < a:
                print("No")
    t -= 1        
        
