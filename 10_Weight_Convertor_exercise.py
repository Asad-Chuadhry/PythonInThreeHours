print("** Weight Convertor **")
weight= float(input("Weight: "))
weightUnit=input("(K)g or (L)bs: ")

if weightUnit.upper()=='K':
    print("Weight in lbs: "+ str(weight/0.45))
elif weightUnit.upper()=='L':
    print("Weight in kg: "+str(weight*0.45))
else:
    print("Wrong Input")

#41
