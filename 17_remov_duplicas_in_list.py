print("** Remove Duplicate in a list **")
numbers=[1,2,4,3,5,6,4,6,7,3,7,9,0,8,6,7]
uniqeNumbers=[]
print(numbers)
for item in numbers:
    if item not in uniqeNumbers:
        uniqeNumbers.append(item)
print(uniqeNumbers)