def myfun(n):
    return lambda x:x+n
m = myfun(12) # n = 12 ,creating one funtion m
print(m)
print(m(9))   # x = 9
k = myfun(78) # n = 78 , creating another function k
print(k(7))   # x = 7