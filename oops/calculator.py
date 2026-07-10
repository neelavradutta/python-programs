class calc:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        
        
    def add(self):
        print("Addition of the numbers are ",self.num1+self.num2)
    
    
    def subs(self):
        print("Substraction of the numbers are ",self.num1-self.num2)
        
        
    def multi(self):
        print("MUltiplication of the numbers are ",self.num1*self.num2)
        
        
    def div(self):
        if self.num2!=0:
            print("Division of the numbers are ",self.num1/self.num2) 
        else:
            print("not divisible")
        
    def mod(self):
        if self.num2!=0:
            print("Modulus of the numbers are ",self.num1%self.num2)
        else:
            print("modulous not possible")
        
num1=int(input("Enter first number "))
num2=int(input("Enter second number "))

self=calc(num1,num2)
self.add()   
self.subs() 
self.multi()
self.div()
self.mod()    