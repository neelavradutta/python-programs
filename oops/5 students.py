class students():
    def __init__(self,marks,total,perc):
        self.marks=[]
        self.total=0
        self.perc=0

    def in_marks(self):
        for i in range(5):
            n=int(input("enter marks of subjects"))
            self.marks.append(n)
    
    def calcper(self):
        self.perc=(sum(self.marks)/5)*100
        
self=students()
print("marks are",self.marks)
print("total =",sum(self.marks))
print("percentage =",self.calcper)
    
            
    
        
        