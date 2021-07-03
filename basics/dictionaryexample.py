data = {1: 'Jane',
        2: 'JOhn',
        3: 'Doe',
        4: 'Mary',
        5: 'Janee'}

print(data.get(2, 'Not Found'))

"""Dictionary of lists"""
keys = ['Jane', 'JOhn', 'Doe', 'Mary']
values = ['Java', 'Python', 'Kafka', 'Javascript']
data = dict(zip(keys, values))

print(data)

data['johnny'] = 'C++'

print(data)

prog = {'JS': 'Atom', 'CS': 'VSCode', 'PYthon': ['pycharm', 'sublime'],
        'Java': {'JSE': 'Netbeans', 'JEE': 'Eclipse'}}

print(prog)

print(prog['JS'])

"""Nested access"""
print(prog['Java']['JEE'])
