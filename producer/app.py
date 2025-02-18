from flask import Flask, jsonify
import random

app = Flask(__name__)
@app.route('/data', methods=['GET'])
def send_data():
	return jsonify({"random_number": random.randint(1,100)})
	
if __name__ =='__main__':
	app.run(host= '0.0.0.0', port=5000)
