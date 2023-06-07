import psycopg2
import pandas as pd
import geopandas as gpd
import folium
from folium.plugins import HeatMap
from shapely.geometry import Point
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
conn.close()

geometry = [Point(xy) for xy in zip(df['LONGITUDE'], df['LATITUDE'])]
geo_df = gpd.GeoDataFrame(df, geometry=geometry)

m = folium.Map(location=[40.7128, -74.0060], zoom_start=11)

gradient = {0.2: 'blue', 0.4: 'lime', 0.6: 'orange', 1: 'red'}

heat_data = [[row['LATITUDE'], row['LONGITUDE']] for index, row in geo_df.iterrows()]

HeatMap(heat_data, gradient=gradient, radius=15, blur=10).add_to(m)

m.save('accidents_map.html')
