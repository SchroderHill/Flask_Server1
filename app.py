from flask import Flask, jsonify
from flask_cors import CORS
import json, os

app = Flask(__name__)
CORS(app)        # ← this enables CORS for every route

DATA_PATH = os.path.join(os.path.dirname(__file__), 'points.geojson')

@app.route("/points")
def get_points():
    if not os.path.exists(DATA_PATH):
        return jsonify({"error": "not found"}), 404
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
