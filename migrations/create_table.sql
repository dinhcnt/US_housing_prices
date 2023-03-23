CREATE TABLE IF NOT EXISTS us_housing (
    id serial PRIMARY KEY, 
    region_id VARCHAR(50),
    region_name VARCHAR(100), 
    period_begin DATE, 
    period_end DATE, 
    total_homes_sold INTEGER,
    total_homes_sold_with_price_drops INTEGER,
    median_sale_price INTEGER,
    off_market_in_one_week INTEGER,
    total_new_listings INTEGER

)