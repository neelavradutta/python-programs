class employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary
        
    def showDetails(self):
        print("Role is",self.role)
        print("Department is",self.dept)
        print("Salary is",self.salary)
        
        
self=employee("System engineer","AI","50000")
self.showDetails()        
        
    
class engineer(employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("","","")
        print("Name is",self.name)
        print("Age is",self.age)
        
        
s1=engineer("rahul","25")
s1.showDetails
        
        

