import json
##
def readjson(file: str):
    with open(file, 'r') as e:
        data = json.load(e)
    return data

def incrementage(data):
    for i in data:
        i['age'] += 1
    return data


def writejson(file, data):
    with open(file, "w") as r:
        json.dump(data, r, indent = 2)

def printold(data, filtered_age):
    lst = []
    for i in data:
        if i['age']>filtered_age:
            print(f'{i['name']} is old than 26,{i['name']} is {i['age']} old ')
            lst.append(i)
        
    print(lst)


a=readjson('names.json')
# incrementage(a)
# writejson('names.json', a)
printold(a, 26)
