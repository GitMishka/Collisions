import psycopg2
import pandas as pd
import config


pg_host = "database-1.cueq5a3aruqx.us-east-2.rds.amazonaws.com"
pg_database = "postgres"
pg_user = "postgres"
pg_password = "Manonthemoon123"

conn = psycopg2.connect(
    dbname=pg_database,
    user=pg_user,
    password=pg_password,
    host=pg_host
)

df = pd.read_sql(f"SELECT * FROM motor_vehicle_collisions", conn)
conn.close()

total_accidents = df.shape[0]

accidents_by_borough = df['BOROUGH'].value_counts()

accidents_by_factor = df['CONTRIBUTING_FACTOR_VEHICLE_1'].value_counts()

print(f"Total number of accidents: {total_accidents}")
print(f"Number of accidents by borough: {accidents_by_borough}")
print(f"Number of accidents by contributing factor: {accidents_by_factor}")
