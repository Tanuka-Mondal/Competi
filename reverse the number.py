t = int(input())
while t!=0:
    r = 0
    n = int(input())
    while n!=0:
        x = n%10
        r = r*10 + x 
        n = n//10
    print(r)
    t-=1
