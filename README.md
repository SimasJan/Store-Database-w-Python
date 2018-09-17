Python Database Project Using SQLite3 and PostgresSQL

Files: 
    1) Script1.py
    2) Script2.py
    3) README.md
    4) psql_commands.txt 


--- Script1.py --- 

A simple store database using SQLite3 to Insert, View, Update, Delete 'store' items. 

Requirements: Python3+, SQLite3 
DB: Table: store  | Table Columns: Item, Quantity, Price.
DB Features: Insert, View, Update, Delete.

IMPORTANT! How to use the script?

1. Edit, uncomment line 19, 'create_table()' and run the command 'python script1.py' in the file directory to create a database with the table.
2. Edit the file again and comment out the same line to avoid recreating the same table. 
3. Run the script and follow the commands shown. 
4. Enjoy! 

 --- Script2.py --- 

A simple store database using a Relational Database, PostgresSQL to Insert, View, Update, Delete 'store' items. 

Requirements: Python3+, PostgresSQL, psycopg2 
DB: Table: store | Table Columns: Item, Quantity, Price
DB Features: Insert, View, Update, Delete

IMPORTANT! How to use the script?

1. Install PostgresSQL onto your computer, if you do not have it yet.
2. Create a new database whether via the PostgresSQL client or Terminal. (terminal command: createdb database1). P.S. If you have changed the database name from 'database1', you will have to change all lines in the script where the connection lines are (dbname='your_database_name'). 
3. Lunch the PostgresSQL server.
4. Run the python script in the terminal. 
5. Follow the commands printed.
6. Enjoy!


-- psql_commands.txt -- 

A short introductory commands and examples of how to create and use PostgresSQL to work with the databases.

