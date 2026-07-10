class circle:
    def __init__(self,r):
        self.r=r

    def get_circle(self):
        print("area of the circle is",3.14*(self.r**2))

class square:
    def __init__(self,a):
        self.a=a
           
    def get_square(self):
        print("area of the square is",self.a**2)
        
class rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    
    def get_rec(self):
        print("area of the rectangle is",self.l*self.b)


n=int(input("enter the radius "))
self=square(n)
self.get_square()


    
        

 
    
        
        