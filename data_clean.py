import psycopg2
import pandas as pd
import numpy as np
import config

pg_host = config.pg_host
pg_database = config.pg_database
pg_user = config.pg_user
pg_password = config.pg_password

conn = psycopg2.connect(
    dbname=pg_database,
    user=pg_user,
    password=pg_password,
    host=pg_host,
    sslmode='require'
)
table_name = "motor_vehicle_collisions"
df = pd.read_sql(f"SELECT * FROM {table_name}", conn)

print("Number of duplicate rows: ", df.duplicated().sum())

df = df.drop_duplicates()

print("Missing values per column: ")
print(df.isnull().sum())

# drop rows with missing latitude or longitude, uncomment the following line
# df = df.dropna(subset=['LATITUDE', 'LONGITUDE'])

print("Columns with single unique value: ")
print(df.columns[df.nunique() <= 1])

print(df.describe())

print("Unique categories in BOROUGH: ")
print(df['BOROUGH'].value_counts())
conn.close()
