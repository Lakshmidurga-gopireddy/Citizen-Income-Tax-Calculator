type_of_citizen=input("Enter type of citizen:")
income=int(input("Enter income:"))
if(type_of_citizen== "individual"):
    if(income<250000):
        tax=0
    elif(income<=500000):
        tax=income*0.05
    elif(income<=1000000):
        tax=12500+income*0.2
    else:
        tax=112500+income*0.3
    print("tax:",tax)
elif(type_of_citizen=="seniorCitizen"):
    if(income<300000):
        tax=0
    elif(income<=500000):
        tax=income*0.05
    elif(income<=1000000):
        tax=10000+income*0.2
    else:
        tax=110000+income*0.3
    print("tax:",tax)
elif(type_of_citizen=="superSeniorCitizen"):
    if(income<=500000):
        tax=0
    elif(income<=1000000):
        tax=income*0.2
    else:
        tax=100000+0.3
    print("tax:",tax)  