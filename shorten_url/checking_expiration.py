import json,datetime
from datetime import datetime

with open('D:\\Python\\PluralSight Course\\Technion Course\\Technion_Files\\project\\shorten_url\\short_urls.json', 'r') as e:
    data = json.load(e)
    print('')

for i in data:
    expiration = datetime.strptime(i['exp'], '%d/%m/%Y')
    if expiration < datetime.now():
        data.remove(i)
with open('D:\\Python\\PluralSight Course\\Technion Course\\Technion_Files\\project\\shorten_url\\short_urls.json', 'w') as w:
    json.dump(data, w, indent = 2)

print('')