t = int(input())
def fact(x):
    if x == 1 or x == 0:
        return 1 
    else:
        return(x*fact(x-1))
while(t!=0):
    n = int(input())
    print(fact(n))
    t -= 1 
