t = int(input())
while(t!=0):
  n = int(input())
  l = list(map(int,input().split()))
  l = sorted(l)
  sum = l[0]+l[1]
  print(sum)  
  t-=1  
