r = int(input())
while(r>0):
    l = int(input())
    s = input()
    a = ""
    if s.count(".") == len(s):
        print("Valid")
    else:
        for i in range(len(s)):
            if (s[i]=="H" or s[i]=="T"):
                a += s[i]
        if (len(a)%2 != 0):
            print("Invalid")
        else:    
            for i in range(0,len(a),2):
                if a[i] =="H" and a[i+1] == "T":
                    b = 1
                else:
                    b = 0
                    break
            if b == 1:
                print("Valid")
            else:
                print("Invalid")
    r-=1            
