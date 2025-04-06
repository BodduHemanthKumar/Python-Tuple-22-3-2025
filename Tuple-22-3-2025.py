# Task:-: 

# Task1 Take a list of dictionary{Name: ,age: ,citize: } check whether that person is eligible for vote or not and also check the citizen.if both conditions are True add { eligible: True}
# details = {
#     "name": "hemanth",
#     "age" : 27,
#     "citizen" : "indian"    
# }
# if details["age"]>=18 and details["citizen"]== "indian":
#     details["eligible"] = True
#     print(details)
#     print("true you are eligible")
# else:
#     details["eligible"] = False
#     print("false you are not eligible")


# Task2: Take a tuple of elements, print the unique elements in the new list

new_tuple = (1,2,1,2,1,3,4,4,5,6,7,3,8,7,9)
unique_elements = list(set(new_tuple))
print(unique_elements)