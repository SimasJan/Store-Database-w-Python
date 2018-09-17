import sqlite3
import sys

# STEPS of working with Databases
    # 1 Connect to a database
    # 2. Create a cursor object
    # 3. Write an SQL query
    # 4. Commit changes
    # 5. Close database connection

def create_table():
    # creating an sql database table.
    conn=sqlite3.connect('lite.db') # creating a connection
    cur = conn.cursor() # creating a cursor object
    cur.execute("CREATE TABLE store (item TEXT, quantity INTEGER, price REAL)") # write an sql query
    conn.commit() # commiting the changes
    conn.close() # close database connection

def insert(item,quantity,price):
    # inserting files to a database
    conn=sqlite3.connect('lite.db') # creating a connection
    cur = conn.cursor() # creating a cursor object
    cur.execute("INSERT INTO store VALUES (?,?,?)", (item,quantity,price))
    conn.commit()
    conn.close()

def view():
    # view the database content
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    # view the database content
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity,price,item))
    conn.commit()
    conn.close()

print('-'*35)
print('Insert data to database | Press 1')
print('View database items     | Press 2')
print('Delete database items   | Press 3')
print('Update database items   | Press 4')
print('-'*35)

while True:
    user_input = int(input('Enter your option or type "0" to exit: '))
    if user_input == 1:
        insert_input = input('Enter ITEM NAME, QUANTITY, PRICE:')
        sliced = insert_input.split(',')
        insert(sliced[0],sliced[1],sliced[2])
    elif user_input == 2:
        print(view())
    elif user_input == 3:
        delete_item = input('enter ITEM NAME to delete: ')
        delete(delete_item)
    elif user_input == 4:
        update_item = input('Enter QUANTITY, PRICE, ITEM to update:')
        sliced = update_item.split(',')
        print(sliced)
        update(sliced[0],sliced[1],sliced[2])
    elif user_input == 0:
        print('Closing Connection.\n Application Ended!')
        sys.exit()
    else:
        print('Option not recognized. Try Again!')
