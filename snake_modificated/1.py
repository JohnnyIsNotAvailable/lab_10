import psycopg2

conn = psycopg2.connect("dbname=suppliers user=postgres password=postgres")

cur = conn.cursor()
        
# execute a statement
print('PostgreSQL database version:')
cur.execute('SELECT version()')

# display the PostgreSQL database server version
db_version = cur.fetchone()
print(db_version)
       
# close the communication with the PostgreSQL
cur.close()