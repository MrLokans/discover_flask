import sqlite3

with sqlite3.connect("app.db") as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS posts")
    c.execute("CREATE TABLE posts(title TEXT, description TEXT)")
    c.execute('INSERT INTO posts VALUES("First Post", "Hello, World!")')
    c.execute('INSERT INTO posts VALUES("Second Post", "Hello, World, again!")')
