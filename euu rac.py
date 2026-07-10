class student:
    
    def __init__(self,name,sub1,sub2,sub3):
        self.name=name
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3
        
    def get_avg(self):
        print("the avg is",(self.sub1+self.sub2+self.sub3)/3)
        
self=student('sreya',45,9,78)
print(self.name),self.get_avg()
