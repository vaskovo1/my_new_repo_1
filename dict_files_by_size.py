import os
from pprint import pprint


def main(path):
    '''
    search files
    '''
    for item in os.listdir(path):
        new_path = os.path.join(path, item)
        if os.path.isdir(new_path):
            main(new_path)
        else:
            allocation(new_path)

def allocation(file):
    '''
    file distribution by size
    '''
    for i in range(len(steps)):
        if os.path.getsize(file) < steps[i]:
            lists[i].append(file[file.rfind('.') + 1:])
            sets[i].add(file[file.rfind('.') + 1:].lower())
            break        


path = r'your_path'

steps = [10**2, 10**3, 10**4, 10**5, 10**6, 10**7, 10**8, 10**9, 10**10] ## on demand

lists = [[] for _ in range(len(steps))]

sets = [set() for _ in range(len(steps))]

dct = {}


main(path)

for i in range(len(steps)):
    dct[steps[i]] = len(lists[i]), sets[i]

for key,value in dct.items():
    dct[key] = list(value)

pprint(dct)





