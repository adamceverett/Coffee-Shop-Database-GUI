from tkinter import *
import sqlite3

# Set parameters for tkinter root window

root = Tk()
root.title("Coffee Shop Database Entry System")
root.geometry("470x470")

# Connect to sqlite database for coffee shop

conn = sqlite3.connect('coffeeshop.db')
cursor = conn.cursor()

# Function for entering new records to customer relation

def submit_customer():
    conn = sqlite3.connect('coffeeshop.db')
    cursor = conn.cursor()

    # SQL Query to insert data input by user into the correct attributes in customer relation from database

    cursor.execute("INSERT INTO customer VALUES (:customer_id, :home_store, :customer_name, :customer_email, :customer_since, :loyalty_card_number, :birthdate, :gender)",
            {
                'customer_id': customer_id.get(),
                'home_store': home_store.get(),
                'customer_name': customer_name.get(),
                'customer_email': customer_email.get(),
                'customer_since': customer_since.get(),
                'loyalty_card_number': loyalty_card_number.get(),
                'birthdate': birthdate.get(),
                'gender': gender.get()
            })

    conn.commit()
    conn.close()

    # To clear previously entered values from entry boxes after submit button is clicked

    customer_id.delete(0, END)
    home_store.delete(0, END)
    customer_name.delete(0, END)
    customer_email.delete(0, END)
    customer_since.delete(0, END)
    loyalty_card_number.delete(0, END)
    birthdate.delete(0, END)
    gender.delete(0, END)

# Function to query the database to show the details of the last record entered

def query_customer():
    
    conn = sqlite3.connect('coffeeshop.db')
    cursor = conn.cursor()

    cursor.execute("SELECT *, oid FROM customer")
    records = cursor.fetchall()

    # for loop will display the values for the last record in the customer table of the database

    print_records = ''
    for i in records[-1]:
        print_records += str(i) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row = 10, column = 0, columnspan = 5, ipadx = 100)

    conn.close()


# Create fields to enter attributes for new customer record in database

customer_id = Entry(root, width = 30)
customer_id.grid(row = 0, column = 1, padx = 20)
home_store = Entry(root, width = 30)
home_store.grid(row = 1, column = 1, padx = 20)
customer_name = Entry(root, width = 30)
customer_name.grid(row = 2, column = 1, padx = 20)
customer_email = Entry(root, width = 30)
customer_email.grid(row = 3, column = 1, padx = 20)
customer_since = Entry(root, width = 30)
customer_since.grid(row = 4, column = 1, padx = 20)
loyalty_card_number = Entry(root, width = 30)
loyalty_card_number.grid(row = 5, column = 1, padx = 20)
birthdate = Entry(root, width = 30)
birthdate.grid(row = 6, column = 1, padx = 20)
gender = Entry(root, width = 30)
gender.grid(row = 7, column = 1, padx = 20)

# Create the labels for the entry boxes

customer_id_label = Label(root, text = "Customer ID")
customer_id_label.grid(row = 0, column = 0)
home_store_label = Label(root, text = "Home Store #")
home_store_label.grid(row = 1, column = 0)
customer_name_label = Label(root, text = "Name")
customer_name_label.grid(row = 2, column = 0)
customer_email_label = Label(root, text = "Email")
customer_email_label.grid(row = 3, column = 0)
customer_since_label = Label(root, text = "Customer Since")
customer_since_label.grid(row = 4, column = 0)
loyalty_card_number_label = Label(root, text = "Loyalty Card Number")
loyalty_card_number_label.grid(row = 5, column = 0)
birthdate_label = Label(root, text = "Birth Date")
birthdate_label.grid(row = 6, column = 0)
gender_label = Label(root, text = "Gender")
gender_label.grid(row = 7, column = 0)

# Create button to submit information entered to our database

entry_button = Button(root, text = "Add Entry to Database", command = submit_customer)
entry_button.grid(row = 8, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

# Create button to show the last entry in the database

query_button = Button(root, text="Show Last Entry into Database", command = query_customer)
query_button.grid(row = 9, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)


conn.commit()
conn.close()

root.mainloop()
