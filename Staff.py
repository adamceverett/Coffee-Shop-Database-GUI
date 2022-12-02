import pandas as pd
import sqlite3

# Data cleaning and insertion into SQLite database for staff.csv

df = pd.read_csv('staff.csv')

# CSV file has additional empty columns that we must drop

df = df.drop("Unnamed: 6", axis = 1)
df = df.drop("Unnamed: 7", axis = 1)

# Changing the locations to correct int value, and FL (future location) to empty string

df = df.replace(to_replace=r'WH', value = 2, regex = True)
df = df.replace(to_replace=r'HQ', value = 2, regex = True)
df = df.replace(to_replace=r'FL', value = '', regex = True)

# Date conversion to proper SQL format

df['start_date'] = pd.to_datetime(df.start_date)
df['start_date'].dt.strftime('%Y-%m-%d')
df['start_date'] = pd.to_datetime(df['start_date']).dt.date


conn = sqlite3.connect('coffeeshop.db')
cursor = conn.cursor()

df.to_sql(name = "staff", con = conn, if_exists = 'replace', index = False)

# Set NULL values for staff without an assigned location

set_null = "UPDATE staff SET location = NULLIF(location, '')"
cursor.execute(set_null)

conn.commit()
conn.close()
