test = int(input())
while test>0:
    f,b,t,d = map(int,input().split())
    rd = d 
    tt = 0
    while b<rd:
        tt = tt + (b*t + f*t)
        rd = rd - (b-f)
    else:
        tt = tt + rd*t 
    print(tt)
    test = test-1        