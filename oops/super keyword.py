class A:
    
    def __init__(self,name):
        self.name=name
        
    @staticmethod
    def foe():
        print("hi")
        
    @staticmethod
    def doe():
        print("hello")
        
        
class B(A):
        
    def __init__(self,go,name):
        self.go=go
        self.name=name            
        super().__init__(name)
        super().foe(),super().doe()
            
    
self=B("reddit",'88')
print(self.name)