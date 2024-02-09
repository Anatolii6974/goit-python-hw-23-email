import os
import django
import configparser
from pymongo import MongoClient

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quotes_scrape.settings")
django.setup()

from qtsapp.models import Author, Quote


config = configparser.ConfigParser()
config.read('utils/config.ini')

mongo_user = config.get('MongoDB', 'mongo_user')
mongodb_pass = config.get('MongoDB', 'mongodb_pass') 
domain = config.get('MongoDB', 'domain')

uri = MongoClient(f"mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/?retryWrites=true&w=majority""", ssl=True)
db = uri.test

authors = db.author.find()
for author in authors:
    Author.objects.get_or_create(
        fullname=author['fullname'],
        born_date=author['born_date'],
        born_location=author['born_location'],
        description=author['description']
    ) 

quotes = db.quote.find()

for quote in quotes:
    print(f'{quote=}')
    exist_quote = bool(len(Quote.objects.filter(quote=quote['quote'])))
    print(f'{exist_quote=}')
    
    if not exist_quote:
        author = db.author.find_one({"_id": quote["author"]})
        # print(f'{author=}')
        a = Author.objects.get(fullname=author["fullname"])
        print(f'{a=}')
        q = Quote.objects.create(quote=quote["quote"], author=a, tags=quote["tags"])


    