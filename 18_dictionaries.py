print("** dictionaries **")
#Keys are must be unique
customer={
    "name": "Asad Mehmood",
    "age": 19,
    "is_verified": True
}
print(customer["name"])
#print(customer["Name"]) KeyError
#another way to access a key value. if key doesn't exist it returns None
print(customer.get("age"))
#print(customer.get("Age")) return None becuase dictionary not have a key named as Age
print(customer.get("birthdate","19-jan-2021")) #if key deosn't exists then it return the default value specified in second argument
print(customer)
#we can add new key values just like
customer["birthday"]="10-43-3433"
print(customer)
# for item in customer:
#     print(customer[item])


