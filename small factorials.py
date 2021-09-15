# cook your dish here

def fact(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * fact(x-1)

t = int(input())    
while (t != 0):
    n = int(input())
    ans = fact(n)
    print(ans)
    t -= 1
    
