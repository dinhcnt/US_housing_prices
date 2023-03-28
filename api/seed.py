import pandas as pd
from sqlalchemy import create_engine

csv = "src/data/weekly_housing_market_data_most_recent.tsv000"
usecols = ['region_id', 'region_name', 'period_begin', 'period_end',
'total_homes_sold', 'total_homes_sold_with_price_drops', 'median_sale_price',
'off_market_in_one_week', 'total_new_listings']
df = pd.read_csv(csv, sep='\t', usecols=usecols, nrows = 5000)
conn_string = 'postgresql://christinadinh@localhost/housing'
engine = create_engine(conn_string)
conn = engine.connect()
df.to_sql('us_housing', conn, if_exists = 'replace')

# results = connection.execute(my_query).fetchall()
