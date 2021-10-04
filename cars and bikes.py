# cook your dish here
t = int(input())
while (t>0):
    n = int(input())
    if (n % 4 == 0):
        ans = "NO"
    else:
        ans = "YES"
    print(ans)
    t -= 1
