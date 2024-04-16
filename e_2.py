from e_1 import *
final = {}
a = readjson('departments.json')
for i in a['departments']:
    sum_age = 0
    for s in i['employees']:
        sum_age += s['age']
    i['employees'].append({'avg_age':(sum_age/len(i['employees']))})
    print(f'In department {i['name']} the avg age is {sum_age/len(i['employees'])}')
    print(i)



print('')