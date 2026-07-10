class circle:
    
    def __init__(self,radius):
        self.radius=radius
        
        
    @staticmethod
    def get_area():
        print("Area of the circle is",3.14*self.radius **2)
        
    @staticmethod
    def get_perimiter():
        print("Perimiter of the circle is",2*3.14*self.radius)    
    
        
self=circle(2)
print("the radius is",self.radius)
self.get_area()
self.get_perimiter()



s1=circle(5)
print("the radius is",self.radius)
s1.get_area()
s1.get_perimiter()
    