print("** Strings **")
course= 'Python for Beginners'
print(course.upper())
print(course.lower())
# return the index of character or word found first
print(course.find('y'))
# return -1 if character or word not found
print(course.find('Y'))
print(course.find('for'))
print(course.replace('for','4'))
#if the word or character is not found in string then it return the orignal string without any change
print(course.replace('x','4'))

#the Find() method return the index of char found first.
# there is another operator 'in' to check that the sub string is present or not
# the 'in' operator return True or False
print('Python' in course)
print('test' in course)


print(course)