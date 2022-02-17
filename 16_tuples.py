#tuple is immutable list(its value cannot be changed after assignment)
#it have no function like appent insert etc
print("** Tuples **")
tuplee=(1,2,3,4,5,5)
print(tuplee)
for item in tuplee:
    print(item)
print("end")
print(tuplee.count(5))
print(tuplee[3])
#tuplee[3]=4 error, object does not support assignment
#unpacking tuples
coordinates=(3,5,4)
print(coordinates)
x,y,z=coordinates
print(x)
print(y)
print(z)
x=50
print(coordinates)
print(x)