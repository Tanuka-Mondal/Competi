try:
    T = int(input())
    while(T!=0):
        A,B = map(int,input().split())
        rem = A % B
        print(rem)
        T -= 1
except:
    pass
