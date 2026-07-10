s1 = "sjfnkaeiorgarj84ajf30dqm.Dmnduicuinoiushhd8INE"
count=0
s2=[]
for i in range(len(s1)):
    if s1[i] in 'aeiou':
        s2.append(s1[i])
        count=count+1
        
    else:
        pass
        
print(s2)
print(count)
        

        
    