import csv
import psycopg2

# Define database connection parameters
host="localhost",
database="phone_book",
user="postgres",
password=" "

# Connect to the database and create a cursor object
conn = psycopg2.connect(dbname=database, host=host, user=user, password=password)
cur = conn.cursor()

def upload_data_from_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=";")
        next(reader)
        for row in reader:
            first_name, last_name, phone, email = row
            cur.execute(
                "INSERT INTO PhoneBook (first_name, last_name, phone, email) VALUES (%s, %s, %s, %s)",
                (first_name, last_name, phone, email,)
            )
        conn.commit()
        print("Data uploaded successfully from", filename)
# Call the function to upload data from a CSV file
filename = "mydata.csv"
upload_data_from_csv(filename)

# Close the cursor and database connection
cur.close()
conn.close()
