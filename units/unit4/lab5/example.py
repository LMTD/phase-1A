# from typing import List
import json
import boto3

# s3 = boto3.client('s3')

class Student():
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
    @classmethod  
    def from_json(cls, data):
        ## to return a Student from json
        return cls(**data)
class Team():
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
# data = json.dumps(team.__dict__, indent=4)

# print(data)


# Deserializing
decoded_team = Team.from_json(json.loads(data))
# decoded_team = json.loads(data)

# print(decoded_team)
# print(decoded_team.students)



def save_custom_obj_to_json(python_data):
  with open('class_test.json', 'w') as output_file:
    json.dump(python_data, output_file, default=lambda o: o.__dict__, sort_keys=True, indent=4) 

def save_to_s3():
    boto3.client('s3').upload_file('class_test.json', 'lmtd-class', 'heyclass.json')

def load_from_s3():
    boto3.client('s3').download_file('lmtd-class', 'heyshafan.json', 'heyclass.json')

def read_from_s3():
    obj = boto3.resource('s3').Object('lmtd-class', 'heyshafan.json')
    print(type(obj))
    data = json.load(obj.get()['Body']) 
    print(data)

save_custom_obj_to_json(team)

# save_to_s3()

# load_from_s3()

read_from_s3()


def load():
  with open('test.json', 'r') as json_file:
    data = json.load(json_file)
    decoded_team = Team.from_json(data)
    print(decoded_team)
    # return data

# load()