from flask import Flask, jsonify
import json

app = Flask(__name__)

# Load JSON data once when the app starts
with open('data.json', 'r') as file:
    data = json.load(file)

@app.route('/data/course/', methods=['GET'])
def get_all_data():
    # Return all data if no ID is provided
    return jsonify(data)

@app.route('/data/course/<entity_id>', methods=['GET'])
def get_entity_by_id(entity_id):
    # Filter the entity with the given ID
    result = next((item for item in data if item['course'] == entity_id), None)
    
    if result:
        return jsonify(result)  # Return the matched entity
    else:
        return jsonify({"error": "Entity not found"}), 404  # Return 404 if not found

if __name__ == '__main__':
    app.run(debug=True, port=8000)
