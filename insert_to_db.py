import sqlite3
import pandas as pd



conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

c.execute('Create table')