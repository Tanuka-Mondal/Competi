import functools
lis = [1,3,5,7,9]
print("SUM : ",end="")
print(functools.reduce(lambda a,b : a+b,lis))