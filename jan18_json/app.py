from flask import Flask, jsonify
import json

app = Flask(__name__)

# Load JSON data ONCE when the app starts
with open('data.json', 'r') as file:
    data = json.load(file)

@app.route('/data/course/', methods=['GET'])
def get_all_data():
    return jsonify(data)

@app.route('/data/course/<entity_id>', methods=['GET'])
def get_entity_by_id(entity_id):
    result = next((item for item in data if item['course'] == entity_id), None)
    
    if result:
        return jsonify(result)
    else:
        return jsonify({"error": "Entity not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=8008)
