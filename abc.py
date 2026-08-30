import sqlite3

conn = sqlite3.connect("test.db",check_same_thread=False)

cursor=conn.cursor()

cursor.execute("""
    INSERT INTO todos VALUES (2,"nefow",FALSE);
""")

conn.commit()
