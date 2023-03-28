# from src.clean import state_region_clean
# from src.orm import build_class
# from src.models import regions
from src import *
from settings import DATABASE, USER
from flask import Flask, jsonify
import psycopg2

conn = psycopg2.connect(database = 'housing', user = 'postgres')
cursor = conn.cursor()
cursor.execute('SELECT * FROM us_housing LIMIT 10;')
records = cursor.fetchall()
region_obj = build_class(Region, records[1])

