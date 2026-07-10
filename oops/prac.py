class student:
    print("Enter Students name and marks respectively")
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def get_average(self):
        sum=0
        for i in self.marks:
            sum=sum+i
        print(self.name,"avg is",sum/3)
                
self=student("Neel",[56,8,92])
self.get_average()
s1=student("rui",[46,80,42])

s1.get_average()

