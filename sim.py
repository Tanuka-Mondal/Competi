def sim_int(p,n,r):
    return (p*n*r)/100

p,n,r = map(int,input("Enter p,n,r: ").split())    
print(sim_int(p,n,r))