t = int(input())
while(t>0):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    l = [0]
    for i in range(n):
        for j in range(n):
            if (a[i]+a[j]+((a[i]-a[j])%m) > l[0]):
                l.append(a[i]+a[j]+((a[i]-a[j])%m))
                l.pop(0)
    print(l[0])            
    t -= 1
