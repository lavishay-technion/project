import datetime
from datetime import datetime
import random
import string
import json



def shorten_url(long_url, jsonfile: str,expiration ):
    char = ''.join(random.choices(string.ascii_lowercase, k=5))
    exists = False
    with open(jsonfile, 'r') as e:
        data = json.load(e)
    for i in data:
        if i['long'] == long_url:
            exists = True
            print(f'URL Already exists, the short url is:{i['short']}')
    if exists == False:
        short_url = f'short.com/{char}'
        istrue = True
        while istrue is True:
            istrue = check_unique(data, short_url)
        data.append({'long':long_url, 'short': short_url, 'exp':expiration})
        with open(jsonfile, 'w') as r:
            json.dump(data, r, indent = 6)
    


def check_unique(jsonfile, text):
    jsonfile = jsonfile
    stext = text
    for i in jsonfile:
        for key in i:
            if key==text:
                return True
    return False

shorten_url("https://github.com/lavishay-technion/",'short_urls.json' , datetime(2024, 4, 17).strftime("%d/%m/%Y"))