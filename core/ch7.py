# The complete python course
# We will use ipy integration in code to execute chunks of code
# to execute a chunk of code just use `# %%` And
# Ctrl+ Enter will execute the code

# %% DBs in Py, example project
import db
import sqlite3
# global books

# %%
conn = sqlite3.connect('db.db')

cursor = conn.cursor()
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS books(name text primary key, author text)')
conn.commit()
conn.close
# %% SELECT
cursor = conn.cursor()
cursor.execute(f'SELECT * FROM Books')
r = [{"name": r[0], "author": r[1]} for r in cursor.fetchall()]
print(r)
conn.commit()
conn.close

# %% INSERT

cursor = conn.cursor()
cursor.execute(f'INSERT INTO books values ("Juan", "Juan")')
conn.commit()
conn.close

# %% INSERT w statements


cursor = conn.cursor()
# Avoid SQL Injection
rs = cursor.execute(f'INSERT INTO books values (?, ?)', ("Juan5", "Juan"))
print(rs)
conn.commit()
conn.close

# %% Using CTX Manager, you can create your own as excersice
with conn:
    cursor = conn.cursor()
    # Avoid SQL Injection
    rs = cursor.execute(f'INSERT INTO books values (?, ?)', ("Juan6", "Juan"))
    print(rs)
    conn.commit()
