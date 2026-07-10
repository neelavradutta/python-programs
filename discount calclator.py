amount=int(input("Enter the amount "))
if amount<1000 and amount!=0:
    print("payable amount is ",round(95/100*amount,2))

elif amount>=1000 and amount<5000:
    print("payable amount is ",round(90/100*amount,2))
    
elif amount>=5000:
    print("payable amount is ",round(85/100*amount,2))
    
else:
    print("no discount")