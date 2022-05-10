l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
ol = list(filter(lambda x:(x%2!=0),l))
el = list(filter(lambda x:(x%2==0),l))
print(ol)
print(el)