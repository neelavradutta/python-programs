class student:
    def __init__(self,name):
        self.name=name
        
self=student("rahul")
print(self.name)

del self
print(self.name)