
list=[1,5,6,4,56,9,5,25,6,5,8,526,29,5,959,26,"dlpls","dgdd","dfdfd","yuy","erg"]

def rof(list,idx=0):
    if idx==len(list):
        return
    print(list[idx])
    rof(list,idx+1)
        
print(rof(list))        