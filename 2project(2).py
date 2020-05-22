import sqlite3

def connect(dbname):
    conn =sqlite3.connect(dbname)

    conn.excuete("CREATE TABLE IF NOT EXIST OYO_HOTELS (NAME TEXT, ADDRESS TEXT, PRICE LIST, AMENITIES TEXT, RATING TEXT)")

    print("Table created successfully11!")

    conn.close()

def insert_into_table(dbname, values):
    conn = sqlite3.connect(dbname)
    print("Inserted into tables: " +str(values))
    insert_sql = "INSERT INTO OYO_HOTELS (NAME,ADDRESS,PRICE,AMENITIES,RATING) VALUES (?, ?, ?, ?, ?)"

    conn.excuete(insert_sql, values)

    conn.commit()
    conn.close()

def get_hotel_info(dbname):
    conn = sqlite3.connect(dbanme)

    cur = conn.cursor()

    cur.excuete("SELECT * FROM OYO_HOTELS")

    table_data = cur.fetchall()

    for record in table_data:
        print(record)
