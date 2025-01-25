from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Load data from external JSON file
with open('dataj25.json', 'r') as file:
    data = json.load(file)


@app.route('/all', methods=['GET'])
def get_all_data():
    return jsonify(data)

@app.route('/all/<program_type>', methods=['GET'])
def get_program_type(program_type):
    # valid_program_types = ["undergraduate", "postgraduate"]  # Define valid program types
    # if program_type not in valid_program_types:
    #     return jsonify({"error": f"Invalid program type '{program_type}'. Valid types are: {', '.join(valid_program_types)}"}), 400

    # Directly use program_type as a key in the data dictionary
    filtered_data = data["Programs"].get(program_type)
    
    if filtered_data:
        return jsonify({program_type: filtered_data})
    else:
        return jsonify({"error": "Program type not found"}), 404

@app.route('/all/<program_type>/<category>', methods=['GET'])
def get_category(program_type, category):
    # program_type = program_type.replace("-", " ")  # Handle spaces in URLs
    # category = category.replace("-", " ")  # Handle spaces in URLs
    program_data = data["Programs"].get(program_type)
    if program_data and category in program_data:
        return jsonify({category: program_data[category]})
    else:
        return jsonify({"error": "Sub-program not found"}), 404

@app.route('/all/<program_type>/<category>/<institute>', methods=['GET'])
def get_institute(program_type, category, institute):
    # program_type = program_type.replace("-", " ")  # Handle spaces in URLs
    # category = category.replace("-", " ")  # Handle spaces in URLs
    # institute = institute.replace("-", " ")  # Handle spaces in URLs

    program_data = data["Programs"].get(program_type)
    if program_data:
        category_data = program_data.get(category)
        if category_data:
            institute_data = category_data.get(institute)
            if institute_data:
                return jsonify({institute: institute_data})
            else:
                return jsonify({"error": f"Institute '{institute}' not found in category '{category}'"}), 404
        else:
            return jsonify({"error": f"Category '{category}' not found in program type '{program_type}'"}), 404
    else:
        return jsonify({"error": f"Program type '{program_type}' not found"}), 404

@app.route('/all/<program_type>/<category>/<institute>/<degree>', methods=['GET'])
def get_degree_programs(program_type, category, institute, degree):
    program_type = program_type.replace("-", " ")  # Handle spaces in URLs
    category = category.replace("-", " ")  # Handle spaces in URLs
    institute = institute.replace("-", " ")  # Handle spaces in URLs
    degree = degree.replace("-", " ")  # Handle spaces in URLs

    program_data = data["Programs"].get(program_type)
    if program_data:
        category_data = program_data.get(category)
        if category_data:
            institute_data = category_data.get(institute)
            if institute_data:
                degree_data = institute_data.get(degree)
                if degree_data:
                    return jsonify({degree: degree_data})
                else:
                    return jsonify({"error": f"Degree '{degree}' not found in institute '{institute}'"}), 404
            else:
                return jsonify({"error": f"Institute '{institute}' not found in category '{category}'"}), 404
        else:
            return jsonify({"error": f"Category '{category}' not found in program type '{program_type}'"}), 404
    else:
        return jsonify({"error": f"Program type '{program_type}' not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088)
