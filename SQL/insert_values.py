
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

# Insert a row into the "posts" table using parameterized queries
cur.execute("INSERT INTO posts (post_id, post_text, user_id) VALUES (%s, %s, %s)", (2, 'I am inserting values to the database using python', 1))

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
