import psycopg2

# Connect to the database
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    user="user",
    password="password",
    database="socratica"
)

# This line creates a cursor, which is an object that allows you to execute SQL queries and fetch the results
cur = conn.cursor()

#This line executes a SQL query to select all rows from the "chitter_user" table
cur.execute("SELECT * FROM chitter_user")

#This line fetches all the rows returned by the SQL query and stores them in the table 
results = cur.fetchall()


