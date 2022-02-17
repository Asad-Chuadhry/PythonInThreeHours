try:
    age = int(input('Age: '))
    income = 2000
    risk = income/age
    print(age)
    print(risk)
except ValueError:
    print('Invalid Value')
except ZeroDivisionError:
    print('Age Cannot be zero.')
