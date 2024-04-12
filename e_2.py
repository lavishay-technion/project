from e_1 import *
final = {}
a = readjson('departments.json')
for i in a:
    for a in a[i]:
        sum_age = 0
        department = a['name']
        for s in a['employees']:
            sum_age += s['age']
        print(f'In department {department} the avg age is {sum_age/len(a['employees'])}')




print('')