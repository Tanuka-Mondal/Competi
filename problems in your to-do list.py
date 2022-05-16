t = int(input())
while(t>0):
    n = int(input(" "))
    d = list(map(int,input(" ").split()))
    b = []
    for i in range(len(d)):
        if (d[i]>=1000):
            b.append(d[i])
    print(len(b))  
    t -= 1
