import pandas as pd
import sqlite3

# Data cleaning and insertion into SQLite database for 201904 sales receipts.csv

df = pd.read_csv('201904 sales reciepts.csv')

# Dropping unneeded column and replacing 0's with empty strings

df = df.drop("line_item_amount", axis = 1)
df = df.replace(to_replace = 0, value = '', regex = True)

# Date to preferred SQL formatting

df['transaction_date'] = pd.to_datetime(df.transaction_date).dt.date


conn = sqlite3.connect('coffeeshop.db')
cursor = conn.cursor()


df.to_sql(name = "transactions", con = conn, if_exists = 'replace', index = False)

# Setting values where we have no customer_id to NULL in database

set_null = "UPDATE transactions SET customer_id = NULLIF(customer_id, '')"
cursor.execute(set_null)

conn.commit()
conn.close()
