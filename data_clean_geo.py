

import psycopg2
import pandas as pd
from sqlalchemy import create_engine

pg_host = "database-1.cueq5a3aruqx.us-east-2.rds.amazonaws.com"
pg_database = "postgres"
pg_user = "postgres"
pg_password = "Manonthemoon123"
table_name = "motor_vehicle_collisions"  

conn = psycopg2.connect(
    dbname=pg_database,
    user=pg_user,
    password=pg_password,
    host=pg_host
)

df = pd.read_sql(f"SELECT * FROM {table_name}", conn)

df = df.dropna(subset=['LATITUDE', 'LONGITUDE'])

database_url = f"postgresql://{pg_user}:{pg_password}@{pg_host}/{pg_database}"

engine = create_engine(database_url)

cleaned_table_name = "geo_data" 
df.to_sql(cleaned_table_name, engine, if_exists='replace')

conn.close()
