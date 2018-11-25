from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello():
	return jsonify({'test': 'test1'})

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 8000))
	app.run(host='0.0.0.0', port=port,debug=True)