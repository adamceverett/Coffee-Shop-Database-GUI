import pandas as pd
import sqlite3

# Data cleaning and insertion into SQLite database for pastry inventory.csv

df = pd.read_csv('pastry inventory.csv')

# Drop unneeded columns for our schema

df = df.drop(['waste', '% waste'], axis = 1)

# Date to preferred SQL formatting

df['transaction_date'] = pd.to_datetime(df.transaction_date)
df['transaction_date'].dt.strftime('%Y-%m-%d')
df['transaction_date'] = pd.to_datetime(df['transaction_date']).dt.date

conn = sqlite3.connect('coffeeshop.db')
cursor = conn.cursor()

df.to_sql(name = "pastry_inventory", con = conn, if_exists = 'replace', index = False)

conn.commit()
conn.close()
