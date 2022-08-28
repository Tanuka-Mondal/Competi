a = list(map(int,input().split()))
b = []
while len(a) > 1:
    if len(a)%2 == 0:
        for i in range(len(a)//2):
            if i != len(a)-i-1:
                b.append(a[i]+a[len(a)-i-1])
            else:
                b.append(a[i])
        print(b)    
    else:
        for i in range(len(a)//2 + 1):
            if i != len(a)-i-1:
                b.append(a[i]+a[len(a)-i-1])
            else:
                b.append(a[i])
        print(b)    
    a = b
    b = []
