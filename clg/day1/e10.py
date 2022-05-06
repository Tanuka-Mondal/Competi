i = 5
def fun(arg=i):
    return arg 
i = 6
print(fun())    
# output is 5, because when line 2 will be executed, i = 5
print(fun(7))