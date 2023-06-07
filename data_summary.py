from sqlalchemy import create_engine
import pandas as pd
import config

pg_host = config.pg_host
pg_database = config.pg_database
pg_user = config.pg_user
pg_password = config.pg_password

engine = create_engine(f'postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}/{pg_database}?sslmode=require')

table_name = "motor_vehicle_collisions"

df = pd.read_sql(f"SELECT * FROM {table_name}", engine)

total_accidents = df.shape[0]

accidents_by_borough = df['BOROUGH'].value_counts()

accidents_by_factor = df['CONTRIBUTING_FACTOR_VEHICLE_1'].value_counts()

df.to_csv('results.csv', index=False)

print(f"Total number of accidents: {total_accidents}")
print(f"Number of accidents by borough: {accidents_by_borough}")
print(f"Number of accidents by contributing factor: {accidents_by_factor}")
