def calculator(a=3,b=8):
    operation = input("Enter +, -, * or / : ")
    
    if operation == "+":
        print("answer: ",a+b)
    elif operation == "-":
        print("answer: ",a-b) 
    elif operation == "*":
        print("answer: ",a*b)  
    elif operation == "/":
        print("answer: ",a/b)  
    else:
        print("Error")             
#a = int(input("Enter 1st digit: "))
#b = int(input("Enter 2nd digit: "))
calculator()