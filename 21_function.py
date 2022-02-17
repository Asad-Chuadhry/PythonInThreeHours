# Always define function above before calling it in source code.
def greet_user():
    print('Hi there!')
    print('welcome aboard')


def greet_user_by_name(name):
    print(f'Hi {name}!')
    print('Welcome aboard')


# Keyword Argument

def welcome_user(first_name,second_name):
    print(f'Hi {first_name} {second_name}')


# return Value
def square(number):
    return number*number


# always leave two blank lines after a function documented in pip8 as better practice
print("start")
greet_user()
print("finish")
greet_user_by_name('Asad')
greet_user_by_name('Mehmood')
welcome_user(second_name="Malik", first_name="Luqman")
print(square(3))