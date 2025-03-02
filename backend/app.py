from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/count', methods=['POST'])
def count_chars():
    data = request.get_json() or {}
    input_string = data.get('input', '')
    result = {'length': len(input_string)}
    return jsonify(result)

if __name__ == '__main__':
    # Bind to all interfaces so that Docker can expose it
    app.run(host='0.0.0.0', port=5000)