# Inserting a large number of rows to the database in the database
import psycopg2

# Connect to the database
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    user="postgres",
    password="password",
    database="postgres"
)

# Create a cursor
cur = conn.cursor()

# Define a list of tuples containing the values to be inserted
values = []
for i in range(2, 1002):
    values.append((i+1, f'user{i}', f'user{i}@example.com',))

# Insert a row into the "posts" table using parameterized queries
cur.executemany("INSERT INTO chitter_user (user_id, user_name, email) VALUES (%s, %s, %s)", values)

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
