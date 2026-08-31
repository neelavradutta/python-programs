licensePlate = "1s3 PSt"
licensePlate=licensePlate.lower()
ch=""
for i in range(len(licensePlate)):
    if licensePlate[i].islower()==True:
        ch=ch+licensePlate[i]

print(ch)