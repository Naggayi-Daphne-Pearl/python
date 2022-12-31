# Inserting more than one value to the database
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
values = [
    (5, 'MY second example', 1),
    (3, 'Third example', 1),
    (4, ' Fourth example', 1),
]

# Insert a row into the "posts" table using parameterized queries
cur.executemany("INSERT INTO posts (post_id, post_text, user_id) VALUES (%s, %s, %s)", values)

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
