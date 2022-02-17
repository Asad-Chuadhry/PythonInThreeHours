print("** If Statements **")

temperature= int(input("Enter Temperature: "))
if temperature>30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature>20:
    print("It's a nice day")
elif temperature>10:
    print("It's a bit cold day")
else:
    print("It's a cold day")

print("Done")