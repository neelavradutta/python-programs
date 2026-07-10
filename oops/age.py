from datetime import datetime

class person:
    def __init__(self,name,country,dob):
        self.name=name
        self.country=country
        self.dob=dob
        
        
    def get_age(self):
        present=datetime.now().year
        return (present-self.dob)
    
    
n=str(input("Enter your Name "))
c=str(input("Enter your Country "))
d=int(input("Enter your birth year "))
    
    
self=person(n,c,d)
print("Name =",self.name)
print("Country =",self.country)
print("Age =",self.get_age())
