t = int(input())

while(t!=0):
    rev=0
    n=int(input())
    n1=n
    while(n1!=0):
        rev = rev*10+n1%10
        n1 = n1//10
    if(n==rev):
        print("wins")
    else:
        print("loses")
    t-=1 
