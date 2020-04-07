"""Flask App Project."""

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/brkga', methods=['POST'])
@cross_origin()
def brkga():
   data = request.get_json()	
   return jsonify(data)

@app.route('/hello')
@cross_origin()
def index():
    """Return homepage."""
    json_data = {'oiee': 'flask!'}
    return jsonify(json_data)


if __name__ == '__main__':
    app.run()
