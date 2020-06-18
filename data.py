import csv
import pandas as pd
import numpy as np
from system.models import USER

user = "data/USER.csv"
song = "data/SONG.csv"
U = pd.read_csv('data/USER.csv')
S = pd.read_csv('data/SONG.csv')

A = U['1'][1]
print(A)

