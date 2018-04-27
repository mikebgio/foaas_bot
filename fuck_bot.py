#!/usr/bin/#!/usr/bin/env python3

import requests
import json

ROOT = 'https://www.foaas.com/'
HEADER = {
    'Accept': "application/json"
    }





def get_fuck(url,headers):
    r = requests.get(url, headers=headers)
    pjson = json.loads(r.text)
    return(pjson)

def main():
    url = ROOT+'shit/mike'
    print(get_fuck(url,HEADER)['message'])

if __name__ == '__main__':
    main()
