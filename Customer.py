import pandas as pd
import sqlite3

# Data cleaning and insertion into SQLite database for customer.csv

df = pd.read_csv('customer.csv')

# Drop birth_year column and retitle name column

df = df.drop(['birth_year'] , axis = 1)
df = df.rename(columns = {'customer_first-name': 'customer_name'})

# Date to preferred SQL format

df['customer_since'] = pd.to_datetime(df.customer_since).dt.date
df['birthdate'] = pd.to_datetime(df.birthdate).dt.date


conn = sqlite3.connect('coffeeshop.db')
cursor = conn.cursor()


df.to_sql(name = "customer", con = conn, if_exists = 'replace', index = False)

conn.commit()
conn.close()
