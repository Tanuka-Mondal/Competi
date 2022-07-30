def find(n,l,m):
    c = -1
    for i in range(n):
        if l[i] == m:
            c = i
        else:
            continue
    print(c)    
        
n = int(input()) #length of array
l = list(map(int,input().split())) #elements of array
m = int(input()) #target element

find(n,l,m)
