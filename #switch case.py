#switch case
a=int(input("enter number 1 = "))
b=int(input("enter number 2 = "))
op=input("enter operation ")
match op:
    case "+":
         print("result =",a+b)
    case "-":
        
        print("result =",a-b)
    case "*":
        
        print("result =",a*b)
    case "/":
        
        print("result =",a/b) 
    case "%":
        
        print("result =",(a/b)*100)
    case _:
        print("invalid")         
    
    
    

    