# JSON  Serialization and Deserialization
import json

# Serialization (Encoding): Python dict -> JSON string
person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChildren": False,
    "titles": ["engineer", "programmer"]
}

# dumps() converts Python dictionary to formatted JSON string
person_json = json.dumps(person, indent=4, sort_keys=True)
print("Serialized JSON string:\n", person_json)

# dump() writes JSON directly to an external file
with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)

#  Deserialization (Decoding): JSON string -> Python dict
# loads() reads from a JSON formatted string
person_dict = json.loads(person_json)
print("Deserialized Python dict:", person_dict)

# load() reads directly from a JSON file
with open('person.json', 'r') as file:
    loaded_person = json.load(file)
print("Loaded from file:", loaded_person)

#  Custom Object Encoding (JSON cannot serialize custom classes by default)
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User("Max", 27)

def encode_user(obj):
    """Custom serializer function passed to 'default' argument."""
    if isinstance(obj, User):
        return {'name': obj.name, 'age': obj.age, obj.__class__.__name__: True}
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

user_json = json.dumps(user, default=encode_user)
print("Custom Object Encoded:", user_json)

#Custom Object Decoding using object_hook
def decode_user(dct):
    """Custom deserializer function restoring a User instance."""
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct

decoded_user = json.loads(user_json, object_hook=decode_user)
print("Decoded object type:", type(decoded_user))
print("Decoded User attributes:", decoded_user.name, decoded_user.age)