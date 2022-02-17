print("** Range Function **")
numbers = range(5) # returns a range object like range(0-5) excluding 5.
print(numbers)
for number in numbers:
    print(number)
print("end")
numbers=range(5,10)
for number in numbers:
    print(number)
print("end")
numbers=range(-5,-1)
for number in numbers:
    print(number)
print("end")
numbers=range(1,10,2) #where last argument is step
for number in numbers:
    print(number)