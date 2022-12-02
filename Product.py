import pandas as pd
import sqlite3

# Data cleaning and insertion into SQLite database for product.csv

df = pd.read_csv('product.csv')

# Preparing our sub-product relations, to create unique ID values

df['product_group_id'] = df.product_group.astype('category').cat.codes
df['product_category_id'] = df.product_category.astype('category').cat.codes
df['product_type_id'] = df.product_type.astype('category').cat.codes

df['product_group_id'] = df['product_group_id'] + 100
df['product_category_id'] = df['product_category_id'] + 300
df['product_type_id'] = df['product_type_id'] + 1000

# Pulling columns for our 3 new relations, removing duplicates

groupdf = df.filter(['product_group', 'product_group_id'], axis = 1)
groupdf = groupdf.drop_duplicates()
groupdf = groupdf.reset_index()
groupdf = groupdf.drop(['index'], axis = 1)

categorydf = df.filter(['product_category', 'product_category_id'], axis = 1)
categorydf = categorydf.drop_duplicates()
categorydf = categorydf.reset_index()
categorydf = categorydf.drop(['index'], axis = 1)

typedf = df.filter(['product_type', 'product_type_id'], axis = 1)
typedf = typedf.drop_duplicates()
typedf = typedf.reset_index()
typedf = typedf.drop(['index'], axis = 1)

# Pulling out columns for our pricing relation, getting rid of dollar signs preceding values

pricedf = df.filter(['product_id', 'current_wholesale_price', 'current_retail_price'], axis = 1)
pricedf = pricedf.replace(to_replace=r'\$', value = '', regex = True)

# Dropping the necessary columns from the original product dataframe

df = df.drop(['current_wholesale_price', 'current_retail_price', 'product_group', 'product_category', 'product_type'], axis = 1)

conn = sqlite3.connect('coffeeshop.db')
cursor = conn.cursor()

df.to_sql(name = "product", con = conn, if_exists = 'replace', index = False)
pricedf.to_sql(name = "pricing", con = conn, if_exists = 'replace', index = False)
groupdf.to_sql(name = "product_group", con = conn, if_exists = 'replace', index = False)
categorydf.to_sql(name = "product_category", con = conn, if_exists = 'replace', index = False)
typedf.to_sql(name = "product_type", con = conn, if_exists = 'replace', index = False)

conn.commit()
conn.close()
