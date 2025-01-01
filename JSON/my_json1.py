# import json
# f=open('data.json',)

# data=json.load(f)


# for i in data:
#     print(i,data[i])

# print(data)


# import json
# dict={"name":"sunil","department":"dev","company":"Edgeverve"}
# print(type(dict))
# json_object=json.dumps(dict)

# print(json_object)
# print(type(json_object))


import yaml

# data = {
#     'name': 'Sachin',
#     'age': 25,
#     'city': 'Bangalore',
#     'skills': ['Python', 'Data Analytics', 'Machine Learning', 'AI']
# }

# # Write the dictionary to a YAML file
# with open('data.yaml', 'w') as file:
#     yaml.dump(data, file)

# print("Data has been written to data.yaml")


# with open('data.yaml') as file:
#     loaded_data=yaml.safe_load(file)
#     print("data loaded")
#     print(loaded_data)



with open('config.yaml','r') as f:
    prime_service=yaml.safe_load(f)

print(prime_service)
print(prime_service['rest']['url'])

