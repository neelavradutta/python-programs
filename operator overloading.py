class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
        
        
    def number(self):
        print(self.real,"i","+",self.img,"j")
        
        
    def __add__(self,n2):
        newreal=self.real + n2.real
        newimg=self.img + n2.img
        return complex(newreal,newimg)
    
    
    def __sub__(self,n2):
        newreal=self.real - n2.real
        newimg=self.img - n2.img
        return complex(newreal,newimg)
    
    
    def __mul__(self,n2):
        newreal=self.real * n2.real
        newimg=self.img * n2.img
        return complex(newreal,newimg)
    
    
    def __truediv__(self,n2):
        newreal=self.real / n2.real
        newimg=self.img / n2.img
        return complex(newreal,newimg)
            
        
s1=complex(5,6)
s1.number()

s2=complex(8,9)
s2.number()

s3=s1/s2
s3.number()