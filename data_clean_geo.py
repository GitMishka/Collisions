

import psycopg2
import pandas as pd
from sqlalchemy import create_engine
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
df = pd.read_sql(f"SELECT * FROM {table_name}", conn)

df = df.dropna(subset=['LATITUDE', 'LONGITUDE'])

database_url = f"postgresql://{pg_user}:{pg_password}@{pg_host}/{pg_database}"

engine = create_engine(database_url)

cleaned_table_name = "geo_data" 
df.to_sql(cleaned_table_name, engine, if_exists='replace')

conn.close()
