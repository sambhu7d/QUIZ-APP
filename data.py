from sys import platform
import unicodedata
import time
import pip
import os


def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

while True:
    try:
        modules = ['html', 'requests']
        for module in modules:
            install(module)
        break
    except:
        print('Bad Internet Connection')
        time.sleep(5)

import requests as rq
import bs4

parameters ={"amount": 10,"category": 18,"type": "boolean"}

response = rq.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]

