from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def serve_json():
    try:
        # Load the JSON data from file
        with open('data.json', 'r') as file:
            data = json.load(file)  # Properly parse the JSON file
        return jsonify(data)  # Return parsed JSON, not a string
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8000)
