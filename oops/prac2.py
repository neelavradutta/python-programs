class prac:
    def __init__(self,age):
        self._age=age
        
    @property
    def age(self):
        self.age=age
        
        
    @age.setter    
    def age(self,a):
        if self.a<0 :
            print("Age cannot be negative")
            
        else:
            return str(self.a)+" years"    

self=prac(-5)
print(self.age)

self.age=60

print(self.age)
        