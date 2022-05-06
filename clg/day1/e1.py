def fact (n):
    f = 1
    while n>0:
        f = f * n
        n = n-1
    return f 

k = [2,3,4,5,6,7]
for i in k:
    print(fact(i))      

print("##############")      
m = map(fact,k)
print(m)
print(list(m))