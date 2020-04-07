"""Flask App Project."""

from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/brkga', methods=['POST'])
def brkga():
   return jsonify(request.json)

@app.route('/hello')
def index():
    """Return homepage."""
    json_data = {'oie': 'flask!'}
    return jsonify(json_data)


if __name__ == '__main__':
    app.run()
