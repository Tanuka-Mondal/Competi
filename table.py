def table(n):
    return lambda a:a*n
a = int(input())  
x = table(a)   
for i in range(1,11):
    print(x(i))