class shape:
    def area(Self):
        pass
    
    def perimeter(Self):
        pass
    
    
class circle(shape):
    def __init__(self,r):
        self.r=r
        
    def get_area(self):
        print("Area is ",3.14*self.r**2)
        
    def get_peri(self):
        print("Perimeter is ",2*3.14*self.r)
        

class triangle(shape):
    def __init__(self,a,b,c,height):
        self.a=a
        self.b=b
        self.c=c
        self.height=height
        
    def get_area(self):
        print("Area is ",1/2*self.b*self.height)
        
    def get_peri(self):
        print("Perimeter is ",self.a+self.b+self.c)
        
        
        
class rectangle(shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        
        
    def get_area(self):
        print("Area is ",self.length*self.breadth)
        
    def get_peri(self):
        print("Perimeter is ",2*(self.length+self.breadth)) 
        
        
r=int(input("Enter radius "))
self=circle(r)    
self.get_area()
self.get_peri()


a=int(input("Enter side 1 "))
b=int(input("Enter side 2 "))
c=int(input("Enter side 3 "))
height=int(input("Enter height of the triangle "))
self=triangle(a,b,c,height)    
self.get_area()
self.get_peri()


length=int(input("Enter length of the reactangle "))
breadth=int(input("Enter breadth of the reactangle "))
self=rectangle(length,breadth)    
self.get_area()
self.get_peri()

        
        
    