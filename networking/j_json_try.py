import json


data = {
    'l': [1,2,3],
    'p': 3,
    'dct': {
        'a': 'hello'
    }
}




# dict into string
data_string = json.dumps(data)

print(type(data_string))
print(data_string)




# string into dict
data_from_json = json.loads(data_string)

print(type(data_from_json))
print(data_from_json)

