coordinate = ['x','y','z']
value = [3,4,5]
r = zip(coordinate,value)
rl = list(r)
print(rl)
c,v = zip(*rl)
print('c = ',c)
print('v = ',v)