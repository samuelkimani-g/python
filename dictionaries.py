# person = {
#     "Name":"Ken",
#     "Age":16
# }
#Adding an entry
# person["Email"] = "ken@gmail.com"

#Removing Items
# del person["Age"]

#clear 
# person.clear()
# print(person)


# student = {
#     "Name":"Alice",
#     "Age":24,
#     "Email":"alice24@gmail.com"
# }

# print(student.get("Name")) #Returns value of specified key
# print(student.keys()) #Returns only keys


#looping through dictionaries

student = {
    "Name":"Alice",
    "Age":24,
    "Email":"alice24@gmail.com"
}

# for key in student:
#     print(key)

# for value in student.values():
#     print(value)

for key, value in student.items():
    print(f"{key} : {value}")