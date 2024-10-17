from uuid import uuid4
import time

import mysql.connector
from faker import Faker
import random
import pickle
from datetime import datetime, timedelta

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="manyusers"
)

# Create a cursor object
cursor = db.cursor()

# Create a Faker instance
fake = Faker()

data = []
with open('users_file.pkl', 'rb') as f:
    data = pickle.load(f)


result = []

for i in range(2):
    result.extend(data)

batch_size = 100_000
start_time = time.time()
for i in range(0, len(result), batch_size):
    batch = result[i:i+batch_size]
    sql = "INSERT INTO users (first_name, last_name, email, birth_date, gender) VALUES (%s, %s, %s, %s, %s)"
    cursor.executemany(sql, batch)
    db.commit()
    print(f"Inserted {i+batch_size} out of 40,000,000 records")

elapsed_time = time.time() - start_time
print(f"Elapsed time {elapsed_time}")

db.close()