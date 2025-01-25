from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# # Load JSON data ONCE when the app starts
# with open('dataj23.json', 'r') as file:
#     data = json.load(file)
# Load the JSON data once when the app starts
data = {
    "Programs": {
            "undergraduate": {
                "basicappliedscience": {
                    "Dr. G.Y. Pathrikar College of Computer Science & Information Technology": {
                        "courses": [
                            "B Sc Hons. Computer Science",
                            "B Sc Hons. Information Technology",
                            "B Sc Hons. Science",
                            "B Sc Hons. Animation",
                            "B Sc Hons. Robotics",
                            "B Sc Hons. Digital Marketing",
                            "M Sc Data Science (Integrated)"
                        ]
                    },
                    "Institute of Bioscience and Technology": {
                        "courses": [
                            "B Sc Hons. Biotechnology",
                            "B Sc Hons. Bioinformatics",
                            "B Sc Hons. Microbiology",
                            "B Sc Hons. Food Technology & Processing",
                            "B Sc Hons. Food Nutrition & Dietetics",
                            "B Tech Biotechnology",
                            "B Tech Food Processing Technology",
                            "B Tech Biomedical Engineering"
                        ]
                    },
                    "School of Basic & Applied Science": {
                        "courses": [
                            "B Sc Hons. Physics",
                            "B Sc Hons. Chemistry",
                            "B Sc Hons. Mathematics",
                            "B Sc Hons. Statistics",
                            "B Sc Hons. Geology",
                            "B Sc Hons. Home Science",
                            "B Sc Hons. Environmental Science",
                            "B Sc Hons. Zoology",
                            "B Sc Hons. Forensic Science",
                            "B Tech Cosmetic Technology"
                        ]
                    }
                },
                "design": {
                    "Leonardo Da Vinci School of Design": {
                        "courses": [
                            "BFA Applied Art",
                            "BFA Contemporary Art",
                            "BFA Traditional Art and Craft",
                            "B Des Interior Design",
                            "B Des Fashion Design",
                            "B Des Textile Design",
                            "B Des Industrial Design",
                            "B Des Visual Communication"
                        ]
                    }
                },
                "engineering": {
                    "Jawaharlal Nehru Engineering College": {
                        "courses": [
                            "B Tech Chemical Engineering",
                            "B Tech Civil Engineering",
                            "B Tech Computer Science and Engineering",
                            "B Tech Electrical and Computer Engineering",
                            "B Tech Mechanical Engineering",
                            "B Tech Robotics and Artificial Intelligence",
                            "B Tech Mechanical and Mechatronics Engineering (Additive Manufacturing)",
                            "B Tech Electronics and Computer Engineering",
                            "B Tech Artificial Intelligence & Data Science",
                            "Bachelor Architecture"
                        ]
                    },
                    "Institute of Fire Service Engineering": {
                        "courses": [
                            "B Sc Fire and Safety"
                        ]
                    },
                    "University Department of Information and Communication Technology (UDICT)": {
                        "courses": [
                            "B Tech Information Technology",
                            "B Tech AI & ML",
                            "B Tech Data Science"
                        ]
                    },
                    "School of Engineering & Technology": {
                        "courses": [
                            "B Tech Agriculture Engineering",
                            "B Tech Computer Science & Engineering (IoT, Cyber Security)",
                            "B Tech Electrical and Instrumentation Engineering",
                            "B Tech (Integrated) Civil Engineering with Computer Application",
                            "B Tech (Integrated) Computer Science and Engineering (Data Science)",
                            "B Tech (Integrated) Computer Science and Engineering (IoT)",
                            "B Tech (Integrated) Advanced Mechatronics and Industrial Automation",
                            "B Tech (Integrated) Robotics and AI",
                            "B Tech Electronic Engineering (VLSI Design and Technology)",
                            "B Tech (Integrated) Information Technology",
                            "B Tech (Integrated) Electrical and Computer Engineering",
                            "B Tech Computer Science and Design",
                            "B Tech Robotics and Automation"
                        ]
                    },
                    "University Department of Pharmaceutical Sciences": {
                        "courses": [
                            "Bachelor Pharmacy"
                        ]
                    }
                },
                "interdisciplinarystudies": {
                    "Department of Sports, Physical Education & Yog Science": {
                        "courses": [
                            "B P E S Bachelor of Physical Education & Sports"
                        ]
                    },
                    "Department of Education": {
                        "courses": [
                            "B A Hons. Education"
                        ]
                    },
                    "University Department of Music & Theatre": {
                        "courses": [
                            "BPA Music",
                            "BPA Theatre"
                        ]
                    }
                },
                "management": {
                    "Institute of Management & Research": {
                        "courses": [
                            "BBA Hons./ Hons. with Research",
                            "BBA Hons./ Hons. with Research in FinTech",
                            "BBA Hons./ Hons. with Research in Business Analytics",
                            "B Com Hons./ Hons. with Research"
                        ]
                    },
                    "hotelmanagement": {
                        "courses": [
                            "B Sc Hons. Hotel Operations Catering Services",
                            "BBA Hons. in Aviation, Hospitality and Travel & Tourism",
                            "B Sc Hons. Culinary Arts"
                        ]
                    },
                    "Nath School of Business & Technology": {
                        "courses": [
                            "Bachelor Management Studies (BMS)",
                            "BCA Cloud Technology & Information Security",
                            "MCA Digital Product Technology",
                            "MCA Artificial Intelligence - Data Science",
                            "BMS Entrepreneurship, Family Business and Innovation"
                        ]
                    }
                },
                "performingarts": {
                    "MAHAGAMI GURUKUL Center for Performing Arts": {
                        "courses": [
                            "BPA Kathak (Lab and Kathak)",
                            "BPA Odissi (Lab and Gurukul)"
                        ]
                    }
                },
                "socialscience": {
                    "College of Journalism & Mass Communication": {
                        "courses": [
                            "B A International Journalism & Electronic Media",
                            "B A Hons./Reg. with Research in Mass Communication and Media"
                        ]
                    },
                    "Institute of Social Sciences": {
                        "courses": [
                            "Bachelor Social Work (BSW)",
                            "B A Hons. Psychology",
                            "B A Hons. Economics"
                        ]
                    },
                    "School of Film Arts": {
                        "courses": [
                            "B A Hons. Cinematography",
                            "B A Hons. Film Direction",
                            "B A Hons. Film Editing",
                            "B A Hons. Sound Designing & Music Production",
                            "B A Hons. VFX and Animation",
                            "B A Hons. Film Acting",
                            "B A Hons. Production Design & Art Direction"
                        ]
                    },
                    "Department of Photography": {
                        "courses": [
                            "B A Hons. Photography"
                        ]
                    },
                    "Institute of Indian & Foreign Languages": {
                        "courses": [
                            "B A Hons. English"
                        ]
                    },
                    "School of Legal Studies & Research": {
                        "courses": [
                            "Bachelor Law (LL.B.)",
                            "BBA Bachelor of Business Administration and Bachelor of Law"
                        ]
                    }
                }
            },
            "postgraduate": {}
        }

    
}



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
