import random
n=10
hc=0
tc=0
for i in range(n):
    t=random.choice(["H","T"])
    if t=="H":
        hc=hc+1
        
    else:
        tc=tc+1
        
print("HC = ",hc)
print("TC = ",tc)
