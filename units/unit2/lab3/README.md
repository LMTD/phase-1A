# LMTD Phase One - Unit Two - Lab 3

OOP & REST API Requests

## About This Lab

This Lab is designed to extend your knowledge of Object Oriented Programming to build a fully functional application with real-world data. We'll create an OOP program and use a RESTAPI to populate our application to make it more usable.

## About JSON

Javascript Object Notation (JSON) is a text-based data format that is used often to transmit data across a network. The JSON format allows for data to be represented using the basic data types: Strings, Numbers, Arrays, Booleans, and object literals (Dictionaries). This allows you to represent data in a hierarchy that can be stored in it's own file `.json`.

```
sample_json = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}
```

### Working With JSON Data in Python

Python makes it easy to work with JSON data. It supports JSON natively. You can use the built-in package `json` to encode (save) and decode (load) JSON data.

To use the `json` module in your python programs all you need to do is include it in your file like so:

```
import json

```

The process of encoding or saving JSON is usually called **serializiation**, which represents transmitting a *series of bytes* into storage. The process of **deserialization** is the process of decoding or loading data that has been stored in the JSON format. 

#### Serializing JSON data

Simple Python objects are translated into JSON using this conversion:

| Python           | JSON Equivalent |
| ---------------- | --------------- |
| dict             | object          |
| list, tuple      | array           |
| str              | string          |
| int, long, float | number          |
| True             | true            |
| False            | false           |
| None             | null            |

Serialization of JSON is a fairly simple process in Python. Take for instance the following Python dictionary:

```python
data = {
    "artist": {
        "name": "Tupac Shakur",
        "genre": "rap",
        "songs": ["Dear Mama", "Hail Mary", "All Eyez On Me"]
    }
}

```

In order to save this file to disk, you can use Python to write it to a file. You can use the Python context manager to open and write to a .json file.

```python
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)

```

The `json.dump` function takes in two arguments, 1) the data object you are intending to serialize, and 2) the variable representing the open file you intend to interact with.

Some useful keyword argument to add to this function is the `indent` argument which allows you to print your JSON with indentation like so:

```python
json.dump(data, indent=4)
```

#### Deserializing JSON

There is a conversion table for loading JSON as well that works similarly:

| JSON         | Python Equivalent |
| ------------ | ----------------- |
| object       | dict              |
| array        | list              |
| string       | str               |
| number(int)  | int               |
| number(real) | float             |
| true         | True              |
| false        | False             |
| null         | None              |

One thing to note is that this conversion isn't an exact inverse of the serialization. For instance you may save an object as a `tuple`, and be surprised to get a `list` back upon loading. It is important to make sure you check the `type()` of your returned object and convert it when necessary.

```python
>>> blackjack_hand = (8, "Q")
>>> encoded_hand = json.dumps(blackjack_hand)
>>> decoded_hand = json.loads(encoded_hand)

>>> blackjack_hand == decoded_hand
False
>>> type(blackjack_hand)
<class 'tuple'>
>>> type(decoded_hand)
<class 'list'>
>>> blackjack_hand == tuple(decoded_hand)
True
```

In order to load a JSON file we use the `json.load` function and pass in the serialized JSON. 

```python
with open("data_file.json", "r") as read_file:
    data = json.load(read_file)

```

The `json.load` function takes in the variable representing the serialized JSON. This may be from a web based transmission or a saved `.JSON` file like the example above.

One thing to note is that there are two similar functions for serialization and deserialization that people use. `json.dumps` and `json.loads` the `.dumps` function works similarly to the `json.dump` function but it turns the serialized json into a string. The `json.loads` function is used to deserialize json that is stored or transferred as a string.

```python
json_string = """{
    "artist": {
        "name": "Tupac Shakur",
        "genre": "rap",
        "songs": ["Dear Mama", "Hail Mary", "All Eyez On Me"]
    }
}"""

json.dumps(json_string)

data = json.loads(json_string)

```

### Making a API Request for JSON

One of the important uses of JSON data is in the process of handling API requests that transfer data in the .JSON format.

Because of the widespread usage of the JSON format across the web, it is commonly returned as data in the API request process.

An API is an Application Programming Interface, a set of functions (software code) that is defined to allow one application to access data from another application.

There are API's for almost everything. One of the greatest tasks programmers have is to request and transfer data across different software instances and Python makes it very easy to do so using the `requests` module.

To make an API request in Python you can use the `requests` module to do the heavy lifting of performing the HTTP request to the server and return a data response. To start you need to import the `requests` package into your code like so:

```python
import requests
```

The following example from [Real Python](https://realpython.com/python-json/) will show us how we can use both the `requests` module and the `json` module to work with transferred JSON.

```python
import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)
```

This returns a JSON object with TODO's structured like so:

```python
{
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": false
}

```

Now that we have JSON represented in our program we can interact with the data in unique ways, for instance using Python to determine of all the returned TODO's which userId has completed the most tasks:

```python
# Map of userId to number of complete TODOs for that user
todos_by_user = {}

# Increment complete TODOs count for each user.
for todo in todos:
    if todo["completed"]:
        try:
            # Increment the existing user's count.
            todos_by_user[todo["userId"]] += 1
        except KeyError:
            # This user has not been seen. Set their count to 1.
            todos_by_user[todo["userId"]] = 1

# Create a sorted list of (userId, num_complete) pairs.
top_users = sorted(todos_by_user.items(), 
                   key=lambda x: x[1], reverse=True)

# Get the maximum number of complete TODOs.
max_complete = top_users[0][1]

# Create a list of all users who have completed
# the maximum number of TODOs.
users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))

max_users = " and ".join(users)

```

We can print this data out to the console in a grammatically correct way like so:

```python
s = "s" if len(users) > 1 else ""
print(f"user{s} {max_users} completed {max_complete} TODOs")

```

One common usecase for JSON in Python outside of the JSON returned from an API Request would be to use the `json` module to write some JSON to a file in order to save some application data important to the user.

For instance, we could create and save a JSON file that contains the completed TODOs for users that have done the maximum number of tasks.

```python
# Define a function to filter out completed TODOs 
# of users with max completed TODOS.
def keep(todo):
    is_complete = todo["completed"]
    has_max_count = str(todo["userId"]) in users
    return is_complete and has_max_count

# Write filtered TODOs to file.
with open("filtered_data_file.json", "w") as data_file:
    filtered_todos = list(filter(keep, todos))
    json.dump(filtered_todos, data_file, indent=2)

```

This example shows how we can use the `requests` module to get some JSON data back from an API as well as create our own `.json` file storing information that is important to us for later use.

### Encoding/Decoding Custom Python Objects to JSON

Now that we know a bit more about working with JSON, there is a bit more we need to learn in order to use it within our Object Oriented programs.

Remember that JSON is only able to serialize certain basic data types in Python: Lists/Tuples, Dictionaries, Booleans, Numbers, and Strings.

So what happens when you try to serialize a custom class?

```python
import json

class Box:
    # Class attribute
    shape = "Cuboid"

    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

box1 = Box(5,4,3) # instantiating a Box object

json.dumps(box1) # throws an error

```

In this case the function `json.dumps` would raise an exception for a `TypeError`, claiming that the `Object of type 'Box' is not JSON serializable`

This is because our custom class is of a different type than the basic data types allowed in the JSON serialization process.

This is a common problem you'll run into that is easy to fix in Python.

To pass custom class objects to the `json.dump` or `json.dumps` functions, you need to simplify your class object to use the more basic data types.

A common solution is to represent your custom class as a dictionary, so it can be easily converted into JSON data.

#### Serializing Custom Classes as a Dictionary using the __dict__

We already know that the `json` module works well with dictionaries. However our custom classes aren't intrinsically represented as Dictionaries.

Python however makes it easy to convert our custom objects as a dictionary by way of another special method called `__dict__`

This method can be used on any custom object, and just like the `__str__` or `__init__` methods, it allows us to perform some special features on our custom objects.

The `__dict__` function is used to represent your custom object as a dictionary in Python. It works like so:

```python
import json
class Student(object):
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

student = Student(first_name="Jake", last_name="Doyle")
json_data = json.dumps(student.__dict__)
print(json_data)
print(Student(**json.loads(json_data)))

```

```python
#Output
{"first_name": "Jake", "last_name": "Doyle"}
<__main__.Student object at 0x105ca7278>
```

The `__dict__` function can be called on an instance of our Python custom class in order to represent it's basic data as a dictionary. 

The double asterisks `**` in the `Student(**json.load(json_data)` function is used to expand the dictionary while loading it. Meaning it allows us to instantiate our Student object with all of the keys and values in the dictionary. This would be equivalent to this:

```python
d = json.loads(json_data)
Student(first_name=d["first_name"], last_name=d["last_name"])

```

Things can get a little tricky when you're working with a list of custom data or more complicated object structures. For instance if we have a list of Student objects:

```python
import json
class Student(object):
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
class Team(object):
    def __init__(self, students: []):
        self.students = students

student1 = Student(first_name="Jake", last_name="Doyle")
student2 = Student(first_name="Jason", last_name="Durkin")
team = Team(students=[student1, student2])
json_data = json.dumps(team.__dict__, indent=4)
print(json_data)

```

Dumping this list will also throw a `TypeError`. Luckily Python comes through and makes it easy for us to serialize all of the custom objects in our list during the dumping process.

When serializing the data we can use another parameter in the `json.dump` to specify a `default` function which gets called whenever a specific object can't be serialized.

For instance we can use this `default` function to ensure that any custom objects call their own `__dict__` function during the serialization process.

So in the previous example if we replace:

```python
json_data = json.dumps(team.__dict__, indent=4)

```

with

```python
json_data = json.dumps(team.__dict__, lambda obj: obj.__dict__, indent=4)

```

We are passing in a default lambda function that takes the object that can't be serialized and calling it's `__dict__` method so that it serializes properly.

#### Deserializing our Custom Object

Now that we have our object serializing properly, we can try deserializing:

```python
decoded_team = Team(**json.loads(json_data))
print(decoded_team)
```

Remember that the `**` is used to expand the dictionary as it loads from JSON.

This returns an object that looks like this:

```python
{
    "students": [
        {
            "first_name": "Jake",
            "last_name": "Doyle"
        },
        {
            "first_name": "Jason",
            "last_name": "Durkin"
        }
    ]
}

```

The only problem is that list returns our data in the form of dictionaries instead of our custom object!

We can confirm this by checking the type of our list:

```python
type(decoded_team.students[0])

```

Luckily, Python makes it easy to handle this situation by adding a custom helper function in our classes that will allow us to perform the necessary conversions of our JSON into our proper data type.

This would look like so:

```python
class Student(object):
    # ... other code

    @classmethod
    def from_json(cls, data: dict):
        return cls(**data)
class Team(object):
    # ... other code
    @classmethod
    def from_json(cls, data: dict):
        students = list(map(Student.from_json, data["students"]))
        return cls(students)

```

With this code we can now deserialize our entire custom object properly!

The complete code would look like:

```python
import json
class Student(object):
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
    @classmethod
    def from_json(cls, data):
        return cls(**data)
class Team(object):
    def __init__(self, students: []):
        self.students = students
    @classmethod
    def from_json(cls, data):
        students = list(map(Student.from_json, data["students"]))
        return cls(students)
student1 = Student(first_name="Jake", last_name="Foo")
student2 = Student(first_name="Jason", last_name="Bar")
team = Team(students=[student1, student2])
# Serializing
data = json.dumps(team, default=lambda o: o.__dict__, sort_keys=True, indent=4)
print(data)
# Deserializing
decoded_team = Team.from_json(json.loads(data))
print(decoded_team)
print(decoded_team.students)
```

And there you have it! Python makes the JSON serialization and deserialization process very achievable. This usecase is going to come up very often so it's good to familiarize yourself with the process now.  

## Lab 3 Objective

Working with a group, your goal for this Lab is to write an Object Oriented Program that interacts with an API to bring in some custom data. 

Your program has a few requirements: 1) Your program should use at least three classes (one being a data object for your API data) 2) Your program needs to implement the CRUD methods in at least one of your classes 3) Your program should use the `requests` module to interact with an API to bring in custom data 4) Your program should use the `json` module to write some custom json to a file that can be used in your application later and 5) Your program should be broken up into multiple modules/files.

You all can use any API you want to use but we will present some options that may spark some ideas. This Lab is an opportunity to build an application used for any real-world scenario of interest to your group. 

After you've finished with the required tasks your group should try extending your program to do more creative functionality.

## Collaborating as a Group

Your group should [start a new project](https://repl.it/languages/python) and add eachother as collaborators to have one space to write and test your programs.

 Your group should start by breaking down the responsibilities of the work so that each person can be involved in writing at least one part of the class, and that everyone is able to read and present the final program you build. 

## Important Steps

### Step 1 - Define Your Class Interfaces

Start the project by defining your class interfaces meaning the class names, instance methods, and class methods necessary to get your program working.

### Step 2 - Test Your Interfaces

Instantiate some objects with sample data to make sure your class methods and attributes are working as expected.

Add some code to make sure your application doesn't crash without informing the user what occured.

### Step 3 - Test your API request

Use another file to write your API request handler, and test it out to make sure it is successful before actually bringing the data into your program.

### Step 4 - Connect your program to your API data

Work on the process of Serializing/Deserializing the API data to be used in your program.

### Add other functionality and make your code more readable

Now that your program is working make sure you add other functionality to interact with your data more robustly and ensure your program is able to be read by other engineers!

## Some APIs you may like

Here are [15 fun APIs](https://dev.to/biplov/15-fun-apis-for-your-next-project-5053) you may be inspired by.

There is also a great list of public APIs compiled [here on Github](https://github.com/public-apis/public-apis)

## Submission

Please share a copy of your group's REPL link to us via the Lab submission form shared in Slack when you've finished. Continue to work on the project and be prepared for a code review during our next class on Tuesday!

## Resources

* [Request Module](https://requests.readthedocs.io/en/master/)
* [API Integration in Python](https://realpython.com/api-integration-in-python/)
* [Working with JSON Data in Python](https://realpython.com/python-json/)
* [Serialize and Deserialize](https://medium.com/@yzhong.cs/serialize-and-deserialize-complex-json-in-python-205ecc636caa)
* [What is REST](https://restfulapi.net)
* [What is JSON](https://restfulapi.net/introduction-to-json/)
