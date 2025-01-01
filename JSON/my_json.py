import json

# Example: Converting a Python dictionary to JSON
data = {"name": "John", "age": 30}
json_data = json.dumps(data)
print(json_data)

# Example: Parsing JSON back to a dictionary
parsed_data = json.loads(json_data)
print(parsed_data)
