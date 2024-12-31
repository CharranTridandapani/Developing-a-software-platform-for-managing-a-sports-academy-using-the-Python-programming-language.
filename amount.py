amount=int(input("Enter your current amount :"))
day=int(input("Enter n.o of days :"))
i=1
while i<=day:
    print("Day :", i)
    print("Day profit : Rs.", int((amount * 3 / 100)))
    amount=amount+(amount*3/100)
    print("Day amount : Rs.",int(amount))
    i+=1
print("Total Amount after ",day," days : Rs.",int(amount))