class student:
    name='hello'
    
    
    def chng(self,name):
        self.__class__.name='hi'
           
        
self=student()
self.chng("rahul")

print(self.name)
print(student.name)

#self.changename('drass')
#def changename(cls,name):
     #   cls.name=name