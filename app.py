"""Flask App Project."""

from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage."""
    json_data = {'Hello': 'World!'}
    return jsonify(json_data)


@app.route('/brkga', methods=['POST'])
def brkga():
   return jsonify(request.json)

if __name__ == '__main__':
    app.run()
