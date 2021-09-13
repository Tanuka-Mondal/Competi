try:
    T = int(input())
    while(T!=0):
        N = int(input())
        sum = 0
        while(N!=0):
            flag = N%10
            sum += flag
            N = N//10
        print(sum)
        T -= 1
except:
    pass
    
