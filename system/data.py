import csv
import pandas as pd
import numpy as np
from django.db import transaction
sqlite_file = '/home/akshay/Desktop/RecomendedSystem/db.sqlite3'

import sqlite3
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()



U = pd.read_csv('USER.csv')
S = pd.read_csv('SONG.csv')



A = U['1'][1]



