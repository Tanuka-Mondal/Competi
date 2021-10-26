t = int(input())
while(t!=0):
  grade = 0
  h,c,s=map(float,input().split())
  if(h>50 and c<0.7 and s>5600):
    grade = 10
  elif(h>50 and c<0.7):
    grade = 9
  elif(c<0.7 and s>5600):
    grade = 8
  elif(h>50 and s>5600):
    grade = 7
  elif(h>50 or c<0.7 or s>5600):
    grade = 6
  else:
    grade = 5
  print(grade)
  t-=1            
