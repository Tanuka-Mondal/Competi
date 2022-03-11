t = int(input())
while(t!=0):
    S = str(input())
    T = str(input())
    M = str()
    for i in range(5):
        if S[i] == T[i]:
            M += "G" 
        else:
            M += "B" 
    print(M)    
    t-=1   
