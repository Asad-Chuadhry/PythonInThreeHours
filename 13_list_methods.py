print("** List Methods **")
numbers=[1,2,3,4,5]
print(numbers)
#len() => this function is not associated with any Object. we can pass a list to this fun to check its length
print(len(numbers))
# append() => add item to the end of the list
numbers.append(6)
print(numbers)
# insert() => used to add the number in anywhere in the list on the specified index
numbers.insert(0,-1)
print(numbers)
# remove() => remove specified value from the list
numbers.remove(3)
print(numbers)
# IN operator used to check a value present in list or not
print(1 in numbers)
# pop() remove the last number in the list and return
print(numbers.pop())
[print(numbers)]
# index() get the value of a index
print(numbers.index(4))
print(numbers)
#count() returns the count of a value
print(numbers.count(5))
#clear() => empty the list
numbers.clear()
print(numbers)

#copy() to copy a list to another
#sort() sort a list itself
#reverse() reverse the list
print("New List")
snumbers=[4,3,5,7,8]
print(snumbers)
snumbers.sort()
print(snumbers)
snumbers.reverse()
print(snumbers)
cnumbers= snumbers.copy()
print(cnumbers)