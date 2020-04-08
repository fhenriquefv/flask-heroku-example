"""Flask App Project."""

from flask import Flask, jsonify, request
import numpy

app = Flask(__name__)

@app.route('/brkga', methods=['POST'])
def brkga():
   data = request.get_json()	
   return jsonify(data)

@app.route('/hello')
def index():
    """Return homepage."""
    json_data = {'oiee': 'flask!'}
    return jsonify(json_data)


if __name__ == '__main__':
    app.run()
