class student:
    
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        
        
    @property    
    def percentage(self):
        return (self.a+self.b+self.c)/3
    
self=student(47,85,94)
print(self.percentage)

self.a=56
print(self.percentage)
