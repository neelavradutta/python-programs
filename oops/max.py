class yo:
    def __init__(self,s):
        self.s=s
      
    def calc(self):
        for i in range(len(self.s)):
            print(self.s[i])
            
        print("total words =",len(self.s))
               
self=yo(["apple","banana","grapes","pumpkin"])
self.calc()

 
    
        
        