# %%

from tkinter import *
import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# THE CODE FOR THIS GUI HAS BEEN SUCCESSFULLY RUN USING INTERACTIVE MODE IN VISUAL STUDIO CODE
# Python 3.8.10(default, Nov 26 2021)
# IPython 7.13.0
# Details included should any compatibility issues arise with IDE

# Setting parameters for the root window

root = Tk()
root.title("Coffee Shop Data Calculations")
root.geometry("450x400")


# Function to Calculate Number of Baby Boomer Customers in the Database

def bboomer():
    
    conn = sqlite3.connect('coffeeshop.db')

    # Run SQL query to find all customers born from 1946-1964, baby boomers.

    df = pd.read_sql_query("SELECT * FROM customer WHERE birthdate BETWEEN date('1946-01-01') AND date('1964-12-31') ", conn)

    # Take the length of the index for the dataframe we've pulled from the database

    bbnumber = len(df.index)

    # Create label to provide result of this query

    bb_label = Label(root, text=f"Customers born 1946-1964: {bbnumber}")
    bb_label.grid(row=2, column=0, columnspan=2)

    conn.commit()
    conn.close()


# Function to Calculate Mean Waste by Location

def m_waste():
    
    conn = sqlite3.connect('coffeeshop.db')
    
    # Import the full pastry_inventory relation as a data frame

    df = pd.read_sql_query("SELECT * FROM pastry_inventory", conn)

    # Calculating waste quantity for each row -> start_of_day - quantity_sold = waste

    df['quantity_wasted'] = df['start_of_day'].sub(df['quantity_sold'], axis = 0)

    # Seperate by location

    df_location3 = df.loc[df['sales_outlet_id'] == 3]
    df_location5 = df.loc[df['sales_outlet_id'] == 5]
    df_location8 = df.loc[df['sales_outlet_id'] == 8]

    # Calculate the number of dates of records for each location in the month

    days_open3 = df_location3['transaction_date'].nunique()
    days_open5 = df_location5['transaction_date'].nunique()
    days_open8 = df_location8['transaction_date'].nunique()

    # Calculation for the average daily waste by location

    totalwaste_3 = df_location3['quantity_wasted'].sum() / days_open3
    totalwaste_5 = df_location5['quantity_wasted'].sum() / days_open5
    totalwaste_8 = df_location8['quantity_wasted'].sum() / days_open8

    # Calculation for the average starting inventory each day by location

    start_3 = df_location3['start_of_day'].sum() / days_open3
    start_5 = df_location5['start_of_day'].sum() / days_open5
    start_8 = df_location8['start_of_day'].sum() / days_open8

    # Calculating the average proportion of waste each day

    mean_3 = totalwaste_3 / start_3
    mean_5 = totalwaste_5 / start_5
    mean_8 = totalwaste_8 / start_8

    # Conversion to percentage format

    percentage_3 = f"Sales Outlet 3: {mean_3:.2%}"
    percentage_5 = f"Sales Outlet 5: {mean_5:.2%}"
    percentage_8 = f"Sales Outlet 8: {mean_8:.2%}"

    # Creating labels to display waste % value for each of the 3 locations

    mean_label1 = Label(root, text=percentage_3)
    mean_label1.grid(row=4, column=0, columnspan=2)
    mean_label2 = Label(root, text=percentage_5)
    mean_label2.grid(row=5, column=0, columnspan=2)
    mean_label3 = Label(root, text=percentage_8)
    mean_label3.grid(row=6, column=0, columnspan=2)

    conn.commit()
    conn.close()

# Function to Generate Histogram of Waste %

# def waste_histo():
    

#     conn = sqlite3.connect('coffeeshop.db')

#     # Import the data from pastry_inventory to data frame

#     df = pd.read_sql_query("SELECT * FROM pastry_inventory", conn)

#     # 

#     df['quantity_wasted'] = df['start_of_day'].sub(df['quantity_sold'], axis = 0)
#     df['waste_percentage'] = (df['quantity_wasted']/ df['start_of_day']*100).round(2)

#     wastedf = df.filter(['waste_percentage'], axis = 1)

#     wastedf.hist(column= 'waste_percentage')

#     conn.close()

def plot():
  
    import matplotlib
    matplotlib.use("TkAgg")
    from matplotlib import pyplot as plt


    conn = sqlite3.connect('coffeeshop.db')
    df = pd.read_sql_query("SELECT * FROM pastry_inventory", conn)

    df['quantity_wasted'] = df['start_of_day'].sub(df['quantity_sold'], axis = 0)
    df['waste_percentage'] = (df['quantity_wasted']/ df['start_of_day']*100).round(2)

    wastedf = df.filter(['waste_percentage'], axis = 1)

    #plt.hist(wastedf)
    wastedf.hist(column= 'waste_percentage', bins = 15, color = '#a89689', edgecolor = 'black', grid=False)
    plt.xlabel('% of Daily Inventory Wasted')
    plt.ylabel('Number of Days per Item')
    plt.title('Distribution of Waste % April 2019')
    


# Buttons for our 3 calculations

babyboomers_button = Button(root, text = "Number of Baby Boomer Customers in Database", command = bboomer)
babyboomers_button.grid(row=1, column=0, columnspan=2, pady=10, padx=10, ipadx=0)

meanwaste_button = Button(root, text = "Mean Waste % By Sales Outlet", command = m_waste)
meanwaste_button.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

histogram_button = Button(root, text = "Display Histogram of Waste %", command = plot)
histogram_button.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


root.mainloop()

# %%
