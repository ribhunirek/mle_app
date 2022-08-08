import sqlite3
import json

# make connections to the json data & new sql database
ads = json.load(open('ads.json'))
connection = sqlite3.connect('database.db')

# connect to schema to instantiate database
with open('schema.sql') as f:
    connection.executescript(f.read())

# inserting json data by iterating through the rows
for key, ad in enumerate(ads):

	query = "INSERT OR IGNORE INTO ads (date, slot_id, device, impressions) VALUES (?, ?, ?, ?)" 
	cur = connection.cursor()
	cur.execute(query, (ad['date'], ad['slot_id'], ad['device'], ad['impressions']))
	cur.close()

print('Instantiating database.db ... \n')
connection.commit()
connection.close()