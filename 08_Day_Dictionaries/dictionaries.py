dog = {}

dog.update({
    'name': 'bello',
    'color': 'black',
    'breed': 'Pinscher',
    'legs': 4,
    'age': 3
    })

print(dog)

student = {
    'first_name': 'Roland', 
    'last_name': 'Sweden', 
    'gender': 'male', 
    'age': 22, 
    'marital status': 'married', 
    'skills': ['typescript', 'python'], 
    'country': 'Germany', 
    'city': 'Berlin',
    'address': '12345 City Street 123'
}

print(len(student))

print(student['skills'], type(student['skills']))

student['skills'].append('ruby')

print(student)

print(student.keys())
print(student.values())
print(student.items())

student.pop('address')

print(student)

del student

# print(student)  not available anymore