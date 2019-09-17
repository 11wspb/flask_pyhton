from flask import Flask, request, jsonify
from SistemClickbait import Sistem
from config import Config

# bootstrap
app = Flask(__name__)
app.config.from_object(Config)

# load class wira
load_sistem = Sistem()

# routing
@app.route('/check_single', methods=['POST'])
def check_single():
	checkup = load_sistem.checkup_single(request.form);
	resp = jsonify(checkup)
	resp.headers.add('Access-Control-Allow-Origin', '*')
	return resp

if __name__ == '__main__':
	app.run()