# import main Flask class and request object
from flask import Flask, request
import sqlite3

# create the Flask app
app = Flask(__name__)

@app.route('/query-example', methods=['POST'])
def query_example():

	request_parameters = request.get_json(force=True)

	#filters for the sql query
	start_time = request_parameters['start_time'] 
	end_time = request_parameters['end_time']
	group_by = request_parameters['group_by']
	device = request_parameters['filter']['device']

	# ad_slot same as slot_id
	ad_slot = request_parameters['filter']['ad_slot'][0]
	ad_slot = int(ad_slot)

	connection = sqlite3.connect('database.db')
	cursor = connection.cursor()

	query = """
				select """ + (",".join(group_by))  + """,
				sum(impressions) as impressions
				from ads
				where
					slot_id = ?
					and date >= ?
					and date <= ?
					and device in (""" + (",".join(["?"] * len(device))) + """)
				group by """ + (",".join(group_by)) 
	
	input_filters = [ad_slot, start_time, end_time] + device
	result = cursor.execute(query, input_filters).fetchall()
	cursor.close()

	rows = []
	row_dict = {}
	
	for row in result:
		row_dict = {}
		for idx, col in enumerate(group_by):
			row_dict[col] = row[idx]

		row_dict["Impressions"] = row[-1]
		rows.append(row_dict)

	return '''<h1>The aggregated output is \n: {}</h1>'''.format(rows)

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
