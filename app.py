from flask import Flask, jsonify, send_file
import json
import os

app = Flask(__name__)

# Path to your GeoJSON file
DATA_PATH = os.path.join(os.path.dirname(__file__), 'points.geojson')

@app.route('/points', methods=['GET'])
def get_points():
    """
    Serves the contents of points.geojson as JSON.
    """
    if not os.path.exists(DATA_PATH):
        return jsonify({"error": "Data file not found"}), 404

    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    # For local testing: listen on all interfaces so e.g. ngrok can tunnel it
    app.run(host='0.0.0.0', port=5000, debug=True)
