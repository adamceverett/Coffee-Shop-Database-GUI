import pandas as pd
import sqlite3

# Data cleaning and insertion into SQLite database for sales_outlet.csv

df = pd.read_csv('sales_outlet.csv')

# Data cleaning record values, dropping columns not needed for schema

df = df.replace({'warehouse': 'warehouse/hq'})
df = df.drop(['manager', 'store_longitude', 'store_latitude'], axis = 1)
df = df.rename(columns = {'Neighorhood': 'neighborhood'})

conn = sqlite3.connect('coffeeshop.db')
cursor = conn.cursor()

df.to_sql(name = "sales_outlet", con = conn, if_exists = 'replace', index = False)

conn.commit()
conn.close()
