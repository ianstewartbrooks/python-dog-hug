import hug
from google.cloud.datastore import Client, Key, Query, Entity

# A simple Hug CRUD REST API that stores the names and ages of dogs in a Google Datastore database.

# Get a dog by it's ID
@hug.get("/dog")
def get_dog(id: hug.types.number):
    client = Client()
    key = client.key("Dog", id)
    dog = client.get(key)

    return {"name": dog["name"], "age": dog["age"]}


# Add a new dog
@hug.post("/dog")
def dog_post(name: hug.types.text, age: hug.types.number):
    client = Client()
    key = client.key("Dog")
    dog_key = key

    dog_entity = Entity(dog_key)
    dog_entity["name"] = name
    dog_entity["age"] = age

    client.put(dog_entity)

    return {"id": dog_entity.key.id}


# Update a dog's info
@hug.put("/dog")
def put_dog(id: hug.types.number, name: hug.types.text, age: hug.types.number):
    client = Client()
    key = client.key("Dog", id)
    dog_key = key

    dog_entity = Entity(dog_key)
    dog_entity["name"] = name
    dog_entity["age"] = age

    client.put(dog_entity)

    return {"id": dog_entity.key.id}


# Delete a dog
@hug.delete("/dog")
def delete_dog(id: hug.types.number):
    client = Client()
    key = client.key("Dog", id)
    client.delete(key)

    return {"message": "dog deleted"}


# Return a list of all dogs in the datastore
@hug.get("/dogs")
def get_all_dogs():
    dogs = []

    client = Client()
    query = Query(client, kind="Dog")

    dogs = query.fetch()

    return {"dogs": dogs}
