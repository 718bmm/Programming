# built-in modules
import math
import os

from pathlib import Path, WindowsPath

# third-package modules
# import pandas as pd
from itertools import *

# my modules
import utils.shop as shp
import db_connection as dbc


print(__name__)



import datetime
posts = [
    {
        'tags': 'django,music',
        'title' : 'Random title',
        'body': 'dasdsadasdsa',
    },
    {
        'tags': 'django, hiking',
        'title' : 'Random title',
        'body': 'dasdsadasdsa',
    },
    {
        'tags': 'django,music',
        'title' : 'Random title',
        'body': 'dasdsadasdsa',
        'published': datetime.date(2023, 5, 12),
    },
    {
        'tags': 'django,music',
        'title' : 'Random title',
        'body': 'dasdsadasdsa',
        'published': datetime.date(2023, 5, 11),
    },
    {
        'tags': 'jazz',
        'title' : 'Random title',
        'body': 'dasdsadasdsa',
    },
]
for post in posts:
    if posts['tags'] == posts['tags'] and posts['title'] == posts['title'] and posts['body'] == posts['body'] and posts['published'] == posts['published']:
        print(post.sorted(0))
    elif posts['published'] == posts['published']:
        print(post.sorted(1))

    print(f"{post['title']}")








