import json

# Open and read the JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

# Print the data
json_text = json.loads(data)
print(json_text)

print(len(json_text))