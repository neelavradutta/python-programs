class college:
    
    @staticmethod
    def name():
        print("My name is")
        
    @staticmethod    
    def dept():
        print("My department is")
        
    
class student(college):
    def __init__(self,go,de):
        self.go=go
        self.de=de
        
self=student("Neel","CSBS")
self.name(),print(self.go)