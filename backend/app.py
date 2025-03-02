from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/count', methods=['POST'])
def count_chars():
    data = request.get_json() or {}
    input_string = data.get('input', '')
    result = {'length': len(input_string)}
    return jsonify(result)

if __name__ == '__main__':
    # Get port from environment variable or use default 5000
    # Note: On macOS, port 5000 may be used by AirPlay Receiver
    # If you encounter "Address already in use" error, set PORT env var to 5001 or 5002
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)