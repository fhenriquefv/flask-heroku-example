"""Flask App Project."""

from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/echo', methods=['POST'])
def hello():
   return jsonify(request.json)

@app.route('/hello')
def index():
    """Return homepage."""
    json_data = {'oi': 'flask!'}
    return jsonify(json_data)


if __name__ == '__main__':
    app.run()
