class prac:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    @staticmethod                                   #decorator
    def get_sum():
        print("the sum is",self.a+self.b)
        
self=prac(4,6)
self.get_sum()

self.a=8
self.b=9
self.get_sum()
        