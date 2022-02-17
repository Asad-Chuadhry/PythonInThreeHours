# this is how we can import a built in module and use this in our code
# there are many python build in module found at "python module index"
import random
print(random.random())
print(random.randint(1, 100))

members = ["Asad", "Mehmood", "Luqman", "Abdullah", "rumi"]
leader = random.choice(members)
print(leader)