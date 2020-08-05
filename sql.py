import sqlite3

# this create a new database is not exist
with sqlite3.connect("blog.db") as conn:
    c = conn.cursor()

    # create the table

    c.execute("create table posts (title text, post text)")

    c.execute('insert into posts values ("Good","I\'m good." )')
    c.execute('insert into posts values ("Well","I\'m well." )')
    c.execute('insert into posts values ("Excellent","I\'m excellent." )')
    c.execute('insert into posts values ("Okay","I\'m okay." )')


