num1=int(input("enter the number 1:"))
num2=int(input("enter the number 2:"))
print(" select\n  1=> addition\n 2=>subtraction \n  3=> multiplication\n 4=> division\n 5=> modulus")
oper=int(input("enter the operation number:"))
match(oper):
    case 1 :
        print(f"addition of {num1} and {num2}:",num1+num2)
        
    case 2: 
        print(f"subtraction of {num1} and {num2}:",num2-num1)
        
    case 3:
        print(f"multiplication  of {num1} and {num2}:",num1*num2)
    
    case 4:
        print(f"division  of {num1} and {num2}:",num1/num2)
        
    case 5:
        print(f"modulus  of {num1} and {num2}:",num1%num2)
    case _:
        print("default input")
        
    